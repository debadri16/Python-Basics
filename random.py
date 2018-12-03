x,y=int(input('Enter starting num ')),int(input('Enter ending num '))
x={str(x) for x in range(x,y+1)}
print(int(x.pop()))