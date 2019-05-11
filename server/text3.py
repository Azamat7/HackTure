import requests
import json

f = open("script_sample.txt", "r")
script = eval(f.read())
f.close()
  
full_text = ""

for s in script:
  if "text" in s:
    full_text += s['text'].strip()

params = "{\"input_data\":[\""
params += full_text[:1000]
params += "\"],\"input_type\":\"text\",\"N\":30}"

r = requests.post("https://unfound-keywords-extraction-v1.p.rapidapi.com/extraction/keywords",
  headers={
    "X-RapidAPI-Host": "unfound-keywords-extraction-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "9840da312emshb785be15f2be366p1b76efjsnbca35920968f",
    "Content-Type": "application/json"
  },
  params=(params)
)

print(r.json())

keyPhrases = r.json()['documents'][0]['keyPhrases']

for key in keyPhrases:
	print("keyWord:", key)

print(keyPhrases)




