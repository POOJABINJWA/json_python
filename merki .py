# import json

# dict1 ={
#     "emp1": {
#         "name": "Lisa",
#         "designation": "programmer",
#         "age": "34",
#         "salary": "54000"
#     },
#     "emp2": {
#         "name": "Elis",
#         "designation": "Trainee",
#         "age": "24",
#         "salary": "40000"
#     },
# }

# out_file = open("myfile.json", "w")
  
# json.dump(dict1, out_file, indent = 6)
  
# out_file.close()



t=int(input("enter the number"))
if  t>=30 and t<=65:
    print("FIRST")
elif t>=50 and t<=90:
    print("SECOND")
elif t==42:
    print("ANY")