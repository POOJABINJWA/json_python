# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho?
import json
p={'4': 5, '6': 7, '1': 3, '2': 4}
print(json.dumps(p, sort_keys=True, indent=4))


















# e=[]
# for i in p:
#     e.append(p[i])
#     for i  in range (len(e)):
#         for j in range (len(e)):
#             if e[i]<e[j]:
#                 tm=e[i]
#                 e[i]=e[j]
#                 e[j]=tm
# print(e)












# dict1={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a=[]
# for i in dict1:
#     a.append(dict1[i])
# k=sorted(a)
# dic={}
# for i in k:
#     for j in dict1:
#         if i==dict1[j]:
#             dic.update({j:dict1[j]})
# print(dic)
# k.reverse()
# dic={}
# for i in k:
#     for j in dict1:
#         if i==dict1[j]:
#             dic.update({j:dict1[j]})
# print(dic)
