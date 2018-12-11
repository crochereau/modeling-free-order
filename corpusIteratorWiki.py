from paths import WIKIPEDIA_HOME
import random
 

def load(language, partition):
  if language == "italian":
    chunks = []
    with open(WIKIPEDIA_HOME+"itwiki/itwiki-"+partition+".txt", "r") as inFile:
      for line in inFile:
        chunks.append(line.strip().lower())
        if len(chunks) > 20000:
           random.shuffle(chunks)
           yield "".join(chunks)
           chunks = []
    yield "".join(chunks)
  else:
    chunks = []
    pathInfix = {"german" : "", "english" : "/enwiki/"}[language]
    with open(WIKIPEDIA_HOME+""+pathInfix+language+"-"+partition+".txt", "r") as inFile:
      for line in inFile:
        chunks.append(line.strip().lower())
        if len(chunks) > 20000:
           random.shuffle(chunks)
           yield "".join(chunks)
           chunks = []
    yield "".join(chunks)

def training(language):
  return load(language, "train")
#   with open(WIKIPEDIA_HOME+""+language+"-train.txt", "r") as inFile:
#     data = inFile.read().strip().lower().split("\n")
#     print("Shuffling")
#     random.shuffle(data)
#     print("Finished shuffling")
#     return "".join(data)
def dev(language):
  return load(language, "valid")
#   with open(WIKIPEDIA_HOME+""+language+"-valid.txt", "r") as inFile:
#     data = inFile.read().strip().lower().split("\n")
#     print("Shuffling")
#     random.shuffle(data)
#     print("Finished shuffling")
#     return "".join(data)
#

#     for line in data:
#        yield line


