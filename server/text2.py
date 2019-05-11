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
text = full_text

r = requests.post("https://proxem-term-extraction-v1.p.rapidapi.com/api/TermExtraction/Extract?method=0&nbtopterms=20",
  headers={
    "X-RapidAPI-Host": "proxem-term-extraction-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "9840da312emshb785be15f2be366p1b76efjsnbca35920968f",
    "Accept": "applications/json",
    "Content-Type": "text/plain"
  },
  params=(text)
)

print(r.json())

keyPhrases = r.json()['documents'][0]['keyPhrases']

for key in keyPhrases:
	print("keyWord:", key)

print(keyPhrases)






