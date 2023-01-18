import json
# print("Content-type text/json")
# print("")
obj=None
with open('D:\pyton23\BYV_PYThON_23_HQ_23\condition.json', 'r') as file:
    obj=json.load(file)
data=json.dumps(obj)
print(data)

# print("Content-type application/json")
# print("")

# import json
# obj = None
# with open("example.json", "r") as file:
#     obj = json.load(file)
# print(json.dumps(obj))