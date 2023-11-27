# lista = [1,5,4,8,2]
# lista.sort()
# print(lista)

# lista.insert(0,100)
# print(lista)

# lista.append("test")
# print(lista)

# lista.pop(0)
# print(lista)

# usuniety=lista.pop()
# print(usuniety)

# lista.remove(4) #usunie wartosc 4, nie index
# print(lista)    #usunie pierwszy element od lewej

# lista.append("test")
# print(lista)

# ind = lista.index("test")
# print(ind)

# lista.reverse()
# print(lista)
# lista2=["siema"]
# print(lista+lista2)

# print(lista.count("test"))


# mojalista = ['pies' , 'piesek' ,1, 4 ,'pies', 'kot', 'pies']
# ilosc=mojalista.count("pies")
# while ilosc>0:
#     print(mojalista.index("pies"))
#     ilosc=ilosc-1

# mojalista = ['pies' , 'piesek' ,1, 4 ,'pies', 'kot', 'pies']
# for i in mojalista:
#     print(mojalista.index("pies"))

# x = range(1,10,4)
# y = []
# for z in x:
#     if z % 2:
#         y.append(z)
# print(y)

# mojalista = []
# for x in range(5,20):
#     if not (x % 3):
#         mojalista.append(x)
# print(mojalista)

# def wiel(x):
#     l=[]
#     for x in range(5):
#         l.append(x+x)

# wiel(4)
# x=3
# y=1
# lista=[]
# for i in range(0,5):
#     x=(x+x)/y
#     lista.append(x)
#     y=y+1
# print(lista)



# def elem(x,y):
#     lista=[]     #<2,6) = 2,4
#     while x<y:
#         if x%2==0:
#             lista.append(x)
#         x=x+1
#     return lista

# elem(2,6)

# lista=[]
# x=2
# y=6     #<2,6) = 2,4
# while x<y:
#     lista.append(x)
# x=x+1
# print(lista)

# x = "technik"
# print (x[-4:-1:2])

# mojalista = ['pies' , 'piesek' ,1, 4 ,'pies', 'kot', 'pies']
# for i in mojalista:
#     print(i)
        # print(mojalista.index("pies"))

# suma =0
# for x in range(1,1001):
#     if x%2==0:
#         suma = x 
# print(suma)

# x = 5
# suma = 0
# for z in range(1,x+1):
#     suma = suma+z
# print(suma)

# x = 2
# suma = 0
# for z in range(1,x+1):
#     suma = suma+(z*z)
# print(suma)
# x=6
# suma = 0
# for z in range(1,x+1):
#     suma = suma+z
# print(suma)

# ile = 10
# for x in range(0,10):
#     ile = ile - 1
#     print(ile)
#     if x == 4:
#         break
# print(ile)


# def silnia(n):
#     if n==0:
#         return 1
#     else:
#         return n*silnia(n-1)

# t=silnia(5)
# print(t)

# from datetime import datetime, timedelta
# now=datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.strftime("%B"))
# print(now.strftime("%w"))
# print(now.strftime("%j"))

# year=("Jan 1 2014 2:43")
# date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
# print(date_object)

# now2=datetime.now().time()
# print(now2)

# days=timedelta(seconds=5)
# print(now+days)

# dic={"key":"value","key2":{"key3":"value3"}}
# try:
#     print(dic['kwy'])
# except KeyError:
#     print("zle klucz wpisales glabie")
# dic2={"keyw": 2, 3: 4, "ttt": 3, 2: 1, 0: 0}
# sorted_dic2=sorted(dic2.items())
# print(sorted_dic2)

# d = {0:10, 1:20}
# print(d)
# d.update({2:10})
# print(d)

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# for i in (dic1,dic2,dic3):
#     dic4.update(i)
# print(dic4)

# x=5
# dic3={5:50,6:60}
# for i in dic3.keys():
#     if x in dic3:
#         print("y")
#     else:
#         print("no")
    
# x=33
# dic3={5:50,6:60}
# if x in dic3.keys():
#     print("y")
# else:
#     print("no")

# n=4
# d={}
# for x in range(1,n+1):
#     d[x]=x*x
# print(d)
# d={}
# for x in range(1,16):
#     d[x]=x*x
# print(d)

# lista = [1,2]
# lista.sort()

# with open("plik.txt","a") as fi:
#     for i in lista:
#         fi.write(str(i))
#         fi.write("\n")

