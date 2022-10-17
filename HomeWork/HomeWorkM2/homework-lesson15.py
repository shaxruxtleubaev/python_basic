
print('1.')
start = 0
stop  = 10
while start < stop:
	start += 1
	print(start, end=' ')
print()

print('2.')
start = 0
stop = 20
process = True
while process:
    start += 1
    if start >= 5 and start <= stop:
        print(start, end=' ')
print()

print('3.')
start = 0
stop = 30
process = True
while process:
    start += 1
    if start >= 1 and start <= 20:
        print(start, end=' ')
print()

print('4.')
start = 0
stop = 50
process = True
while process:
    start += 1
    if start >= 15 and start <= 40:
        print(start, end=' ')
print()

print('5.')
a = 'Привет'
b = 'Hello'
start = 0
stop = 10
process = True
while process:
    start += 1
    if start <= stop:
        print(f'{start}.{a}')
        print(f'{start}.{b}')
print()

print('6.')
USA = 'США'
Russia = 'Россия'
China = 'Китай'
start = 0
stop = 15
process = True
while process:
    start += 1
    if start <= stop:
        print(f'{start}.{USA}')
        print(f'{start}.{Russia}')
        print(f'{start}.{China}')
print()

print('7.')
start = 0
stop = 50
process = True
while process:
    start += 1
    if start <= 30:
        print(f'{start}',end=' ')
print()

print('8.')
a = 15
i = 1
s = 0
while i <= a:
    s += i
    i += 1
    print(s,end=' ')
print()

print('9.')
a = 10
i = 0
s = 1
while i < a:
    i += 1
    s *= i
    print(s,end=' ')
print()

print('10.')
a = 1
b = 5
i = 0
d = 0
while i < b:
    i += 1
    a *= i
    d += a
    print(d,end=' ')
print()













