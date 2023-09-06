# lisx=[1,2,3,4]

# def even_odd(n):
#     if n % 2 == 0:
#         return n+50
#     else:
#         return n+20
# z=map(even_odd,lisx)
# print(list(z))          #[21, 52, 23, 54]
# Assignement 
# 11. # From a given list, find the even nos and then square those and put the squares in the list. 
# 12 From a given list, find the even nos and then square those and put the squares in the list. And then print the sum of the final list.

lisx=[1,2,3,4,5,6,8,9,10]
def even_num(n):
    if n%2 == 0:
        return n
def square_num(n):
    return n**2
even_list=list(filter(even_num,lisx))
square_list=map(square_num,even_list)
even=list(square_list)
print(even)
print(sum(even))





# Output:
# [4, 16, 36, 64, 100]
# 220
