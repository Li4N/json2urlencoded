import json
import urllib.parse

jsonData = input("Insert JSON raw content: ")
dictData = json.loads(jsonData)

dictData['variables'] = json.dumps(dictData['variables'])

encodedData = urllib.parse.urlencode(dictData, quote_via=urllib.parse.quote)

print(encodedData)
