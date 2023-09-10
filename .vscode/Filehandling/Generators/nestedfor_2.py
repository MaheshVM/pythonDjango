out=[
    (n,m) for n in range(1,10) if n%2==0
    for m in range(1,5) if m%2==0
]
print(out)
#[(2, 2), (2, 4), (4, 2), (4, 4), (6, 2), (6, 4), (8, 2), (8, 4)]


print(['even' if x%2==0 else 'odd' for x in range(1,10)])
#['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']
# it indicatesleft side of for can be any expressio you want it
# in comprehension left side of for can be any expression you require.