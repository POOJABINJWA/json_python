
#simple flie certed karna
# a=open("rani.json","w")
# c=a.write("mujhe bhi chaye ")
# print(a)
# a=open("rani.json","r")
# y=a.read()
# print(y)
 



# dump flie write karna
import json
a={"name":"pooja","age":19,"rollno":34}
with open("pooja . json","w")as g:
    json.dump(a,g,indent=12)

#python convert to json
# import json
# p={"name":"jeyesh","city":"kannod","year":2020}
# j=json.dumps(p)
# print(j)
