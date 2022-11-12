
a = int(input("Type a number between 3 and 6: "))

if a%2==0 :
    b = a//2
else :
    b = a//2 + 1

for c in range(a):
    for d in range(a):    # horizontal
        h , i = a - c , a - d
        if d+1<a :
            if b>c and b>d :     #1 quadrante 
                if d>c : print(c+1,end=" ")
                elif c>d : print(d+1,end=" ")
                elif c==d : print(d+1,end=" ")
            elif b>=c+1 and b<d+1 :          #2 quadrante
                if i>c : print(c+1, end=" ")
                elif i==c : print(i, end=" ")
                else : print(i,end=" ")
            elif b<c+1 and b>d+1:            #3 quadrante
                if h>d+1: print(d+1, end=" ")
                elif h==d+1 : print(d+1, end=" ") 
                else : print(h, end=" ")
            elif b<c+1 and b<=d+1:           #4 quadrante
                if i>h: print(h,end=" ")
                elif i==h : print(i, end=" ")
                else: print(i,end=" ")
            elif c==a-1 :                # última linha
                print(1,end=" ")
            else : print(b,end=" ")    # centro
        else : print(1)
        



""" 
for d in range(a):    # horizontal
        if d+1<a or c+1<a :
            if b>c or b>d :
                if d>c :
                    print(d+1,end=" ")
                else: print(c+1,end=" ")
            elif b==c :
                if d>c :
                    print(d+1,end=" ")
                else: print(c+1,end=" ")
            elif c==a-1 :
                print(1,end=" ")
            else :
                print(f, end=" ")
        else :
            print(1)
        f = e - 1  """
