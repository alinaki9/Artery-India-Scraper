import json
import requests
import csv

url_auction = "https://admin.arteryindia.com:8001/api/getAuctions"
image_url = "https://cdn.arteryindia.com/images/thumbnails/"

file = open("auction_ids_test.txt", "r")
file_contents = file.read().splitlines()
file.close()

header = ['auction_id', 'auction_house', 'auction_name', 'auction_location', 'auction_date', 'title', 'image_url', 'lot', 'year_of_creation', 'medium', 'material', 'size', 'estimate_min', 'estimate_max', 'sold_for', 'status', 'artist_name', 'category', 'nationality', 'gender', 'year_of_birth', 'year_of_death']
auction_id = 1
        
for r in file_contents:

    data = {

        "auction_id": r ,
        "filter": {},
        "page": 1,
        "sort": {},
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImNoYW5kcmlrYUBhcnRlcnlpbmRpYS5jb20iLCJfaWQiOiI1ZjdhZTBkM2EwNWU0MjVjMjVkZGU5NTAiLCJmaXJzdF9uYW1lIjoiQ2hhbmRyaWthIiwicGhvdG8iOiIiLCJsZXZlbCI6NiwiaWF0IjoxNjUwMDk2NTU5fQ.hUrNtkqVf0RVv1XW8XZ_jTn5zYdpMkt1EbxL3ww7Xrs",
        "type": "single"

    }

    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url_auction, data = data_json, headers = headers)

    j = r.json()

    num_lots = len(j["data"]["query"])
    print (num_lots)

    with open('test.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        for i in range(0, num_lots):

            data = [auction_id, j["data"]["query"][i]["auction_details"]["auction_house"], j["data"]["query"][i]["auction_details"]["auction_name"], j["data"]["query"][i]["auction_details"]["auction_location"], str(j["data"]["query"][i]["auction_details"]["auction_date"]).split("T")[0], j["data"]["query"][i]["title"], image_url + str(j["data"]["query"][i]["painting_id"]) + ".jpg", j["data"]["query"][i]["lot"], j["data"]["query"][i]["year_of_creation"], j["data"]["query"][i]["material_details"][0]["medium"], j["data"]["query"][i]["material_details"][0]["material"], str(j["data"]["query"][i]["size"][0]["h"]) + " X " + str(j["data"]["query"][i]["size"][0]["w"]) + " Inches", j["data"]["query"][i]["estimate"]["INR"]["est_min"], j["data"]["query"][i]["estimate"]["INR"]["est_max"], j["data"]["query"][i]["price_realised"]["INR"], j["data"]["query"][i]["status"], j["data"]["query"][i]["artist"]["artist_name"], j["data"]["query"][i]["artist"]["category"], j["data"]["query"][i]["artist"]["nationality"], j["data"]["query"][i]["artist"]["gender"], j["data"]["query"][i]["artist"]["yob"], j["data"]["query"][i]["artist"]["yod"]]
            # write the data
            writer.writerow(data)



    #print(j["data"]["query"][0]["artist"])











