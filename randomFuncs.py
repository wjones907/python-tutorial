import random




x = random.random()
y = random.randint(0,100-1)
print 'x, y:',x , y
print 'int(x):', int(x)

go = 0
while go < 10:
    print 'random[index]:',random.randint(1,100)
    go += 1
