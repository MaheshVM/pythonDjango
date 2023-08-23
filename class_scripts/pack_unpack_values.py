fruits=('grapes','banana','cherry','pineapple','blueberry')
print(type(fruits))

(green,*yellow,red) = fruits
# (green,yellow,red) = ('grapes','banana','cherry')
print(green)
print(yellow)
print(red)

