# Script to create application/x-www-form-urlencoded body request parameter from JSON raw input
import json
import urllib.parse


jsonData = input("Insert JSON raw content: ")
dictData = json.loads(jsonData)
encodedData = urllib.parse.urlencode(dictData)

print(encodedData)
