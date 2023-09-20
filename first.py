print('mrinmoy')

a = 6

print(a)
b = 8
print(a)

def run(a):
    b = 9
    print(b)
    print( b)

run(a)

class A:
    z = 4
    def __init__(self , x , y ):
        self.x= x
        self.y= y

    def show(self):
        print(self.x)
        print(b)
        self.c = 9
        print(self.c)

    def run(self):
        print(self.c)    


obj = A(1,2)
obj.show()
print("mbj")
obj.run()

class B(A):
    def __init__(self , x , y ):
        super(x,y)
        self.show()



mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

def remove(l):
    return list(dict.fromkeys(l))
    
li = remove(["a", "b", "a", "c", "c",'m']) 
print(li)   


xx = ' my forst birtday is one 12'

def revers(xx):
    return xx[::-1]

print(revers(xx))

def sum(a,b):
    return (int(a) + int(b))

print(sum(12,12))    


def red(x):
        
    flie = open(x,'a')

    flie.write('\n this is new line writen')
    flie.close()

    flie = open(x,'r')

    for x in flie:
        print(x)


red("x.text")


import os

if os.path.exists('x.text'):
    os.remove('x.text')
    print('complete deleting file ......')
    #os.rmdir("v")
else :
    print('file doesnot exist in computer')





if os.path.exists('html.txt'):
    f = open('cc.txt','x')
    f.write('mhfjkhkfhgk')
    print(f)
    print('yes....')
    os.remove('html.txt')
    print('delete.....')