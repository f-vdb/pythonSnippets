import json

file_Name = "jsonTest.txt"

def pt(argument):
    print(f"{type(argument)} : {argument}")

json_string: str = '''
{
   "book":[
      {
         "id":"444",
         "language":"C",
         "edition":"First",
         "author":"Dennis Ritchie "
      },
      {
         "id":"555",
         "language":"C++",
         "edition":"second",
         "author":" Bjarne Stroustrup "
      }
   ]
}  
'''

pt(json_string)

# loads load string
data = json.loads(json_string)
pt(data)

for book in data["book"]:
    pt(book)

new_Ugly_String = json.dumps(data)
pt(new_Ugly_String)

new_Nice_String = json.dumps(data, indent=2)

pt(new_Nice_String)

with open(file_Name, "w") as f:
    json.dump(data, f, indent=2)

with open(file_Name, "r") as f:
    data = json.load(f)

pt(data)





