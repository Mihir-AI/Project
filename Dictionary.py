import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w in data:
      return data[w]
    elif len(get_close_matches(w,data.keys()))>0:


         yn=input(f"did u mean {get_close_matches(w,data.keys())[0]} instead?Enter Y or N:")
         if yn=="Y":
              return data[get_close_matches(w,data.keys())[0]]
         elif   yn=="N":
                return "we did'nt understand your entry.please check the entry"
         else:
                return "please check the word"

    else:
           return "The word doesn't exist.Please double check it"
word= input("Enter the word:")


output=translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
     print(output)