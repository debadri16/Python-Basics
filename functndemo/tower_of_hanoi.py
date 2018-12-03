def hanoi(a,c,b,num):
    if num==1:
        print('move',num,'disc from',a,'to',c)
        return
    hanoi(a,b,c,num-1)
    print('move', num, 'disc from', a, 'to', c)
    hanoi(b,c,a,num-1)

hanoi('A','C','B',3)