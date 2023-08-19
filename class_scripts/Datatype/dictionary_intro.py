car={
    "brand":"audi",
    'model':'q5',
    'year':2023,        #observe here at the end we put , here. not mandatory
    "variant": "v4",    #at the end add ,
}

print(car)
print(car['brand'])     # say as key not index 
# we can add further key & value to dictionary
car['country']="india"
print(car)
# if same key trying to add it will override with existing
car['brand']="hyundai"  #this modifies previous key and override
print(car)          #{'brand': 'hyundai', 'model': 'q5', 'year': 2023, 'variant': 'v4', 'country': 'india'}


dict2={
    (1,20): "onetwo",           # it is valid key 
    'name':"Mahesh"
}
print(dict2[(1,20)])            #onetwo
#keys with list should not be correct, because it should not be any immutable object

a=(1,2,3,4,5)
d3={
    a:'This is question'
}
print(d3[a])        #This is question, because key a here is immutable because it is tuple here

soft_emp={
    'emp_id':"Mahesh",
    'emp_height':6.5,
    'languages': ['english','kannada','marathi'],
    "address": ('res','office'),
    'M': True,
    "education":{"UG","pg"}
}
print(soft_emp)
print(soft_emp['languages'][-1])        #marathi
print(soft_emp['languages'][-1][2:5])   #rat
print(soft_emp["address"])              #('res', 'office')
print(soft_emp.keys())                  #prints all keys dict_keys(['emp_id', 'emp_height', 'languages', 'address', 'M', 'education'])
print(soft_emp.values())                #prints all values dict_values(['Mahesh', 6.5, ['english', 'kannada', 'marathi'], ('res', 'office'), True, {'pg', 'UG'}])
print(soft_emp.items())                 # prints all the values of dictionary
#dict_items([('emp_id', 'Mahesh'), ('emp_height', 6.5), ('languages', ['english', 'kannada', 'marathi']), ('address', ('res', 'office')), ('M', True), ('education', {'UG', 'pg'})])