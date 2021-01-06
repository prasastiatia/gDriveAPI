 #This code sample uses the 'requests' library:
# http://docs.python-requests.org
import json
import requests
check_item = ['permintaan','kedua']
nama_checklist = ['Permintaan Dokumen','Pengerjaan Pembukuan Bulanan','PPh Pasal 21','PP23']
jml_checklist = [3,6,8,5]
id = []

def create_card(nama):
    url = "https://api.trello.com/1/cards"
    query = {
    'key': '3c78038b2fb7b6a363747a970bd88a8d',
    'token': '5f974000ff8785c961a405faab8aac4954244ea9307bd1c711d5af0946f958dd',
    'idList': '5fe98afecb97fd5f79ffce5b',
    'name': nama
    }
    response = requests.request(
    "POST",
    url,
    params=query
    )
    cardresult = response.text
    print(cardresult)
    d = json.loads(cardresult)
    global id_card
    id_card = d['id']
    print(id_card)  
    return id_card

def create_create_checklist(idc):
    for x in range(len(nama_checklist)):
        url = "https://api.trello.com/1/checklists"
        query = {
        'key': '3c78038b2fb7b6a363747a970bd88a8d',
        'token': '5f974000ff8785c961a405faab8aac4954244ea9307bd1c711d5af0946f958dd',
        'idCard': idc,
        'name' : nama_checklist[x]
        }
        response = requests.request(
        "POST",
        url,
        params=query
        )
        checkresult = response.text
        x = json.loads(checkresult)
        id.append(x['id'])
        print(x['id'])
        print(checkresult)
        print(id)

def create_check_item(id):
    for b in range(len(check_item)):
            js = id[0]
            url = "https://api.trello.com/1/checklists/%s" % js
            url1 = "/checkItems"
            newUrl = "".join((url, url1))
            print(newUrl)
            query = {
                'key': '3c78038b2fb7b6a363747a970bd88a8d',
                'token': '5f974000ff8785c961a405faab8aac4954244ea9307bd1c711d5af0946f958dd',
                'name': check_item[b],
                            }
            response = requests.request(
                    "POST",
                    newUrl,
                    params=query
                )

create_card('testing')
create_create_checklist(id_card)
create_check_item(id)