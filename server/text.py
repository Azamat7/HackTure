import requests
import json

f = open("script_sample.txt", "r")
script = eval(f.read())
f.close()
  
full_text = ""

for s in script:
  if "text" in s:
    line = "'".join(s['text'].strip().split("&#39;"))
    full_text += line
    full_text += " "

full_text = " ".join(full_text.split('\n'))
keyPhrases = []

for i in range(len(full_text)//5000):
  text = full_text[i*5000:(i+1)*5000]

  r = requests.post("https://microsoft-azure-text-analytics-v1.p.rapidapi.com/keyPhrases",
    headers={
      "X-RapidAPI-Host": "microsoft-azure-text-analytics-v1.p.rapidapi.com",
      "X-RapidAPI-Key": "9840da312emshb785be15f2be366p1b76efjsnbca35920968f",
      "Content-Type": "application/json"
    },
    json={
      "documents": [
        {
          "language": "en",
          "id": "string",
          "text": text
        }
      ]
    })
  keyPhrases += r.json()['documents'][0]['keyPhrases']

text = full_text[(len(full_text)//5000)*5000:len(full_text)]
r = requests.post("https://microsoft-azure-text-analytics-v1.p.rapidapi.com/keyPhrases",
  headers={
    "X-RapidAPI-Host": "microsoft-azure-text-analytics-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "9840da312emshb785be15f2be366p1b76efjsnbca35920968f",
    "Content-Type": "application/json"
  },
  json={
    "documents": [
      {
        "language": "en",
        "id": "string",
        "text": text
      }
    ]
  })
keyPhrases += r.json()['documents'][0]['keyPhrases']


#print(r.json())
print("Total %s keyWords \n", len(keyPhrases))

for key in keyPhrases:
	print("keyWord:", key)

print(keyPhrases)
