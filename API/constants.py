APIKEY ='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'
DOCUMENT = './data/data.txt'
DOCUMENT_ROOT = 'data/' 
PERSIST = True
PERSIST_ROOT = 'persist'
RESUME_INDEX = 'resuming index'
LINE_BREAK = '____________________________' 

class ColorWrapper:
  red = "\033[91m"
  green = "\033[92m"
  yellow = "\033[93m"
  blue = "\033[94m"
  magenta = "\033[95m"
  cyan = "\033[96m"
  reset = "\033[0m"

def console(**kwags):
  color = kwags.get('color', ColorWrapper.reset)
  msg = kwags.get('msg', 'no msg')
  reset = kwags.get('reset', False)
  if reset:
    print(f"{color}{msg}{ColorWrapper.reset}")
  else:
    print(f"{color}{msg}")
