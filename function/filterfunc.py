'''
from a given list find the even nos and then square those and put the squares in the list and print the sum of list
filter function:
Create a list find the even number and put in separate list
filter the data based on condition, it works on selective items.
map works on all.
very important: filter function will look into only the condition do not look anything after this
filter function will not do any expression
works only on the selective condition not for any mathematical expressions
anything wanted to filter based on requirement we do use filter function
'''
#numbers=[1,2,3,4,5,6,7,8,9,10]
#numbers=(1,2,3,4,5,6,7,8,9,10)

numbers={1,2,3,4,5,6,7,8,9,10}

# def even_nos(n):
#     if n%2 == 0:
#         return n
# out=filter(even_nos,numbers)
# print(out)                      #<filter object at 0x0000011EBD0EB7C0>
# print(list(out))                #[2, 4, 6, 8, 10]


# lambda aprroach of writing the code
print("---using filter and lambda appraoch---")
#print(list(filter(lambda n:n%2==0,numbers)))

#[2, 4, 6, 8, 10]

#print(tuple(filter(lambda n:n%2==0,numbers)))
# (2, 4, 6, 8, 10)

print(set(filter(lambda n:n%2==0,numbers)))
#{2, 4, 6, 8, 10}

