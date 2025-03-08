import json

j="""
{
"students":[
    {
    "name": "John", 
    "age": 30, 
    "city": "New York"
    },
    {
    "name": "kanehn",
    "age": 29,
    "city": "CHennai"
    }
]
}
"""
d=json.loads(j)
print(d)
print(d['students'][0])    
print("new")
d['test']=True
nj=json.dumps(d,indent=2,sort_keys=True)
print(nj)
 
with open(r'D:\git files\CP\py\random\sam.json','r') as f:
    d=json.load(f)
    print(d)
    f.close()

print(d.items())

with open('dump.json','w') as f:
    json.dump(d,f,indent=2)
    f.close()