import requests
import json

f = open("script_sample.txt", "r")
script = eval(f.read())
f.close()
  
full_text = ""

for s in script:
  if "text" in s:
    full_text += s['text'].strip()

text = "A recurrent neural network (RNN) is a class of artificial neural network where connections between nodes form a directed graph along a temporal sequence. This allows it to exhibit temporal dynamic behavior. Unlike feedforward neural networks, RNNs can use their internal state (memory) to process sequences of inputs. This makes them applicable to tasks such as unsegmented, connected handwriting recognition[1] or speech recognition."
text = full_text[:1000]

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

keyPhrases = r.json()['documents'][0]['keyPhrases']

for key in keyPhrases:
	print("keyWord:", key)

print(keyPhrases)
