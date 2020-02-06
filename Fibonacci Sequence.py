l = [1, 1]
number = int(input('Please type any integer:\n'))
for i in range(0, number - 1):
    x = l[i] + l[i + 1]
    l.append(x)

print('The Fibonacci Sequence is : ', l)
print('The %dth term in the sequence is :' % number, l[number - 1])
