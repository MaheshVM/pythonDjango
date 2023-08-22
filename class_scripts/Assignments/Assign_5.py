#concatenation of 2 dictionary
person={
    "name":"Mahesh",
    "place":"Pune",
    'pin':1234,
}

employmet={
    "work": "IT",
    "experience":7,
    'salary': 200.50
}
person.update(employmet)  
print(person)

# output
# {'name': 'Mahesh', 'place': 'Pune', 'pin': 1234, 'work': 'IT', 'experience': 7, 'salary': 200.5}