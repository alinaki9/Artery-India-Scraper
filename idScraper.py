import json
import requests

url_auction = "https://admin.arteryindia.com:8001/api/getAuctions"

page = 1
list_ids = []


for i in range(1,39):
    data = {

        "auction_id": "",
        "filter": {},
        "page": i,
        "sort": {},
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImNoYW5kcmlrYUBhcnRlcnlpbmRpYS5jb20iLCJfaWQiOiI1ZjdhZTBkM2EwNWU0MjVjMjVkZGU5NTAiLCJmaXJzdF9uYW1lIjoiQ2hhbmRyaWthIiwicGhvdG8iOiIiLCJsZXZlbCI6NiwiaWF0IjoxNjUwMDk2NTU5fQ.hUrNtkqVf0RVv1XW8XZ_jTn5zYdpMkt1EbxL3ww7Xrs",
        "type": "all"

    }

    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url_auction, data = data_json, headers = headers)

    j = r.json()

    for r in range(0,50):
        try:
            list_ids.append(str(j["data"]["query"][r]["_id"]))
        except IndexError:
            break


print(len(list_ids))

textfile = open("auction_ids.txt", "w")
for element in list_ids:
    textfile.write(element + "\n")
textfile.close()










