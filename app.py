from Google import Create_Service
from flask import Flask, render_template, request, json
app = Flask(__name__)


parent_folder = ['Admin', '2020']
sub_folder_admin = ['11. Director Details']
sub_folder_tahun = ['01. Januari']
sub_folder_bulan = ['24. PP23']
parent_id_company = []
parent_id_admin = []
parent_id_tahun = []
parent_id_bulan = []
all_id_folder = []

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showPT')
def showPT():
    return render_template('signUp.html')

@app.route('/addPT',methods=['POST'])
def addPT():
    # read the posted values from the UI
    global _name
    global drive_service
    _name = request.form['inputName']
    if _name :
        CLIENT_SECRET_FILE = 'credentials.json'
        API_NAME = 'drive'
        API_VERSION = 'v3'
        SCOPES = ['https://www.googleapis.com/auth/drive']
        drive_service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        create_company_folder(_name)
        create_parent_folder(parent_folder, parent_id_company[0])
        create_sub_folder_admin(sub_folder_admin, parent_id_admin[0])
        create_sub_folder_tahun(sub_folder_tahun, parent_id_tahun[0])
        create_folder_inside_each_month(sub_folder_bulan, parent_id_bulan)
        create_permission(all_id_folder)
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

def create_company_folder(company_name):
    file_metadata = {
        'name': company_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().create(body=file_metadata, fields='id').execute()
    parent_id_company.append(file.get('id'))
    all_id_folder.append(file.get('id'))
    return print("Succes Create Folder for PT")
def create_parent_folder(parent_folder, parent_id):
    for i, folder in enumerate(parent_folder):
        file_metadata = {
            'name': folder,
            'parents': [parent_id],
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = drive_service.files().create(body=file_metadata).execute()
        if i == 0:
            parent_id_admin.append(file.get('id'))
        else:
            parent_id_tahun.append(file.get('id'))
    return print("Succes Create Folder for Admin and Year")
def create_sub_folder_admin(sub_folder_admin, parent_id):
    for sub_admin in sub_folder_admin:
        file_metadata = {
            'name': sub_admin,
            'parents': [parent_id],
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = drive_service.files().create(body=file_metadata).execute()
    return print("Succes Create Sub Folder Admin")
def create_sub_folder_tahun(sub_folder_tahun, parent_id):
    for sub_tahun in sub_folder_tahun:
        file_metadata = {
            'name': sub_tahun,
            'parents': [parent_id],
            'mimeType': 'application/vnd.google-apps.folder'
        }
        file = drive_service.files().create(body=file_metadata).execute()
        parent_id_bulan.append(file.get('id'))
    return print("Succes Create Sub Folder Year")
def create_folder_inside_each_month(sub_folder_bulan, parent_id):
    for x in range(len(parent_id)):
        for sub_bulan in sub_folder_bulan:
            file_metadata = {
                'name': sub_bulan,
                'parents': [parent_id[x]],
                'mimeType': 'application/vnd.google-apps.folder'
            }
            file = drive_service.files().create(body=file_metadata).execute()
    return print("Succes Create Sub Folder Bulan")
def callback(request_id, response, exception):
    if exception:
        # Handle error
        print(exception)
    else:
        print("Permission Id: %s" % response.get('id'))

def create_permission(all_id_folder):
    file_id = all_id_folder[0]

    batch = drive_service.new_batch_http_request(callback=callback)
    user_permission = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': 'tias1508@gmail.com',
    }

    batch.add(drive_service.permissions().create(
            fileId=file_id,
            body=user_permission,
            fields='id',
    ))

    batch.execute()
    return print("Success Create Permission")

if __name__ == "__main__":
    app.run(debug=True)







