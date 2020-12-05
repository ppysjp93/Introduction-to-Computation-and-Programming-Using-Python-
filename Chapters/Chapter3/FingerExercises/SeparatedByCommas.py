s = '1.23,2.4,3.123'
result = 1.23 + 2.4 + 3.123

num = ''
total = 0
for c in s: 
    if c != ',':
        num = num + c;
    else:
        total = total + float(num)
        num = ''

# Add the final number 
total = total + float(num)

print(result)
print(total)
