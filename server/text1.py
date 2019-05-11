import requests
import json

f = open("script_sample.txt", "r")
script = eval(f.read())
f.close()
  
full_text = ""

for s in script:
  if "text" in s:
    full_text += s['text'].strip()

keyPhrases = []

sentences = full_text.split(".")
print(len(sentences))

# for i in range(100):
#   text = ".".join(sentences[i*3:(i+1)*3])
#   text = "+".join(text.split(" "))
#   text = "https://aylien-text.p.rapidapi.com/concepts?text=" + text + "&language=en"
#   r= requests.get(text,
#     headers={
#       "X-RapidAPI-Host": "aylien-text.p.rapidapi.com",
#       "X-RapidAPI-Key": "9840da312emshb785be15f2be366p1b76efjsnbca35920968f"
#     }
#   )
#   for key in r.json()['concepts'].keys():
#     keyPhrases.append(r.json()['concepts'][key]['surfaceForms'][0]['string'])


for key in keyPhrases:
	print("keyWord:", key)



