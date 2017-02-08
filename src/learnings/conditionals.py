a, b = 11, 10

if a < b:
    print (' a ({})is less than the b({})'.format(a, b))
elif a == b:
    print ('a({}) is equals to b({})'.format(a, b))    
else:
    print('a({}) is not less than b({})'.format(a, b))

print ("a is greater than b" if a > b else "a is less than b")

choices = dict(
        one = "one",
        two = 'two',
        three = 'three',
        four = 'four'
)
va = 'five'
print(choices.get(va,'other'))
