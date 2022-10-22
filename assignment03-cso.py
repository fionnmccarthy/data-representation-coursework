# https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en

from ast import Pass
import requests
import json

# can save in variables below to make universal on CSO
url_Beginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
url_End = "/JSON-stat/2.0/en"
dataset = "FIQ02"

# retrive data
def getAll(dataset):   
    url = url_Beginning + dataset + url_End
    response = requests.get(url)
    return response.json()

# write data to json file
def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

# main method
if __name__ == "__main__":
    getAllAsFile(dataset)
