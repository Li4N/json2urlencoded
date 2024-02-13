import json
import urllib.parse


jsonData = input("Insert JSON raw content: ")
dictData = json.loads(jsonData)
encodedData = urllib.parse.urlencode(dictData)

print(encodedData)
