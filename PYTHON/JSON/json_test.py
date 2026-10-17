import json
x='{ "name":"John", "age":30, "city":"New York"}'
y= json.loads(x)
print(y)

z={
    "name":"John", "age":30, "city":"New York"
}
k=json.dumps(z)
print(k)