person = {
      "name": "Marek",
      "surname": "Banach",
      "age": 25,
      "hobby": ["swimming","excursions"],
      "married": True,
      "phone":{"landline":"123444321","mobile":"777888999"}
   }


print(person['hobby'])
person['surname'] = "Nowak"
person['married'] = "False"
person['gender'] = "male"
person['hobby'].append('bicycle')
person["phone"]={"landline":"123444321","mobile":"777888999","work phone":"313131444"}
print(person)
for key,value in person.items():
      print(f"{key} : {value}")




    


 