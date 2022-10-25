# pip install PyGithub
import requests
import json
from github import Github
from config import config as cfg

# get github key form config.py as above
apikey = cfg["githubkey"]


g = Github(apikey)


private_repo = "fionnmccarthy/aprivateone"


repo = g.get_repo(private_repo)

# get file information from test.txt file in repo
fileInfo = repo.get_contents("test.txt")
#url of file is gotten by below
urlOfFile = fileInfo.download_url

# get contects of the file
response = requests.get(urlOfFile)
contentOfFile = response.text

# change contents of file
newContents = contentOfFile.replace("Andrew", "Fionn")

#update file with chnages and commit to github
gitHubResponse=repo.update_file(fileInfo.path,"updated by program",newContents,fileInfo.sha)

