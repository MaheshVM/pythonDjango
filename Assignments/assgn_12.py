# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Using a lambda function to filter even numbers
# num=[1,2,3,4,5,6,7,8,10]
# # even_sq=lambda x: x**2
# # print(list(map(even_sq,filter(lambda n:n%2==0,num))))

# #output
# #[4, 16, 36, 64]
# num=[1,2,3,4,5,6,7,8,10,12]
# print(list(map(lambda num: num**2,filter(lambda n:n%2==0,num))))

# outpu:
# [4, 16, 36, 64, 100, 144]

num=[1,2,3,4,5,6,7,8,10,12]
print(list(map(lambda x: x**2,filter(lambda num:num%2==0,num))))

# outpu:
# [4, 16, 36, 64, 100, 144]