import requests
import json

def highlight_keywords(keyPhrases):
  f = open("script_sample.txt", "r")
  script = eval(f.read())
  f.close()

  for s in script:
    if "text" in s:
      words = "'".join(s["text"].split("&#39;")).split(" ")
      for i in range(len(words)):
        if words[i] in keyPhrases:
          words[i] = "*"+words[i]+"*"
        else:
          for key in keyPhrases:
            keys = key.split()
            if len(keys)==2 and (keys[0]==words[i] or keys[1]==words[i]):
              words[i] = "*"+words[i]+"*"
      s["text"] = " ".join((" ".join(words).split("\n")))
  
  print(script)


def get_full_script():
  f = open("script_sample.txt", "r")
  script = eval(f.read())
  f.close()
    
  full_text = ""
  for s in script:
    if "text" in s:
      full_text += "'".join(s['text'].strip().split("&#39;"))
      full_text += " "
  return " ".join(full_text.split('\n'))

def get_key_phrases(full_text):
  if True:
    return ['mountain', 'MIT OpenCourseWare', 'neural net', 'chain rule', 'partial derivative', 'Creative Commons license', 'neuron', 'dot product', 'MIT', 'sigmoid function', 'exponential', 'convolution', 'neural net', 'assembly', 'neuron', 'memory', 'GPUs', 'kernel', 'mite', 'neural net', 'green values', 'zn', 'blackboard', 'force', 'zebra', 'giraffe', 'neurons', 'vampire', 'cheetah', 'dn', 'GPUs', 'Boltzmann', 'neurons', 'cheetah', 'school bus', 'test case', 'sigmoid', 'formula', 'mystery', 'algorithm', 'normalizing factor', 'gradient ascent', 'softmax', 'vector', 'partial derivatives', 'neuron', 'noise', 'sigmoid function', 'containership', 'probability', 'neural net', 'prop', 'softmax', 'Boltzmann', 'biologist', 'net.', 'blackboard', 'zebra', 'plague', 'giraffe', 'rerun', 'neuron', 'cheetah', 'cliff', 'sigmoid curve', 'local maximum', 'grasshopper', 'frequency', 'engineering', 'Venice', 'neural net', 'cottage industry', 'cat', 'wolf', 'frequency band', 'toilet', 'baseball', 'barbell', 'artificial intelligence', 'Giraffe', 'Frisbee', 'Russian wolfhound', 'neurons', 'rabbit', 'guitar', 'bird', 'school bus', 'Google', 'saddle', 'rectangle', 'local maximum', 'railroad car']

  keyPhrases = []
  length = len(full_text)

  for i in range(length//5000):
    text = full_text[i*5000:(i+1)*5000]
    text = "+".join(text.split(" "))
    text = "https://aylien-text.p.rapidapi.com/concepts?text=" + text + "&language=en"
    r= requests.get(text,
      headers={
        "X-RapidAPI-Host": "aylien-text.p.rapidapi.com",
        "X-RapidAPI-Key": "9840da312emshb785be15f2be366p1b76efjsnbca35920968f"
      }
    )
    for key in r.json()['concepts'].keys():
      keyPhrases.append(r.json()['concepts'][key]['surfaceForms'][0]['string'])


  text = full_text[(length//5000)*5000:length]
  text = "+".join(text.split(" "))
  text = "https://aylien-text.p.rapidapi.com/concepts?text=" + text + "&language=en"
  r= requests.get(text,
    headers={
      "X-RapidAPI-Host": "aylien-text.p.rapidapi.com",
      "X-RapidAPI-Key": "9840da312emshb785be15f2be366p1b76efjsnbca35920968f"
    }
  )
  for key in r.json()['concepts'].keys():
    keyPhrases.append(r.json()['concepts'][key]['surfaceForms'][0]['string'])

  return keyPhrases



full_text = get_full_script()
keyPhrases = get_key_phrases(full_text)

highlight_keywords(keyPhrases)

#print(keyPhrases)




