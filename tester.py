import json
import requests

nama_checklist = ['Permintaan Dokumen','Pengerjaan Pembukuan Bulanan','PPh Pasal 21','PP23']
jml_checklist =[3,6,8,5]
checkitem_PD = ['permintaan bank statment', 'permintaan laporan penjualan', 'permintaan laporan pembelian']

id =[]

def create_cards(nama):
    url = "https://api.trello.com/1/cards"
    query = {
    'key': '2fb50ddab4bccb72c4f25e03680ae024',
    'token': '9ea8aab5b36bd7671f354d5f6597386683f6aef8c3cfb6f4c224d8b09f43996a',
    'idList': '5fe9639ca4647617995c94e8',
    'name':nama
    }
    response = requests.request(
    "POST",
    url,
    params=query
    )
    cardresult = response.text
    print(cardresult)
    y = json.loads(cardresult)
    global id_cards
    id_cards = y['id']
    print(id_cards)
    return id_cards
    
def create_checklist(idc):

    for x in range(len(nama_checklist)):
            
        url = "https://api.trello.com/1/checklists"
        query = {
        'key': '2fb50ddab4bccb72c4f25e03680ae024',
        'token': '9ea8aab5b36bd7671f354d5f6597386683f6aef8c3cfb6f4c224d8b09f43996a',
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

def create_checkitem(id):

    for b in range(len(nama_checklist)):
        if nama_checklist[b] == 'Permintaan Dokumen':
            ulang = jml_checklist[0]  
            for c in range(ulang):
                    js = id[0]
                    url = "https://api.trello.com/1/checklists/%s" % js
                    url1 = "/checkItems"
                    newUrl = "".join((url, url1))
                    print(newUrl)

                    query = {
                        'key': '2fb50ddab4bccb72c4f25e03680ae024',
                        'token': '9ea8aab5b36bd7671f354d5f6597386683f6aef8c3cfb6f4c224d8b09f43996a',
                        'name': 'cobaa',
                                }

                    response = requests.request(
                        "POST",
                        newUrl,
                        params=query
                    )
        elif nama_checklist[b] == 'Pengerjaan Pembukuan Bulanan':
            ulang = jml_checklist[1]  
            for c in range(ulang):  
                    js = id[1]
                    url = "https://api.trello.com/1/checklists/%s" % js
                    url1 = "/checkItems"
                    newUrl = "".join((url, url1))
                    print(newUrl)

                    query = {
                        'key': '2fb50ddab4bccb72c4f25e03680ae024',
                        'token': '9ea8aab5b36bd7671f354d5f6597386683f6aef8c3cfb6f4c224d8b09f43996a',
                        'name': 'coba',
                                }

                    response = requests.request(
                        "POST",
                        newUrl,
                        params=query
                    )
        
        elif nama_checklist[b] == 'PPh Pasal 21':
            ulang = jml_checklist[2]  
            for c in range(ulang):  
                    js = id[2]
                    url = "https://api.trello.com/1/checklists/%s" % js
                    url1 = "/checkItems"
                    newUrl = "".join((url, url1))
                    print(newUrl)

                    query = {
                        'key': '2fb50ddab4bccb72c4f25e03680ae024',
                        'token': '9ea8aab5b36bd7671f354d5f6597386683f6aef8c3cfb6f4c224d8b09f43996a',
                        'name': 'coba',
                                }

                    response = requests.request(
                        "POST",
                        newUrl,
                        params=query
                    )

        elif nama_checklist[b] == 'PP23':
            ulang = jml_checklist[3]  
            for c in range(ulang):  
                    js = id[3]
                    url = "https://api.trello.com/1/checklists/%s" % js
                    url1 = "/checkItems"
                    newUrl = "".join((url, url1))
                    print(newUrl)

                    query = {
                        'key': '2fb50ddab4bccb72c4f25e03680ae024',
                        'token': '9ea8aab5b36bd7671f354d5f6597386683f6aef8c3cfb6f4c224d8b09f43996a',
                        'name': 'coba',
                                }

                    response = requests.request(
                        "POST",
                        newUrl,
                        params=query
                    )

create_cards('testing')
create_checklist(id_cards)
create_checkitem(id)