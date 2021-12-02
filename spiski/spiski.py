#uezd=['Tallinn','Narva, Narva-Jõesuu','Kohtla-Järve','Ida-Virumaa, Lääne-Virumaa, Jõgevamaa','Tartu linn','Tartumaa, Põlvamaa, Võrumaa, Valgamaa','Viljandimaa, Järvamaa, Harjumaa, Raplamaa','Pärnumaa','Läänemaa, Hiiumaa, Saaremaa']
#while 1:
#    try:
#        ind=int(input("Введи свой индекс: "))
#        if 10000<=ind<=99999:
#            break
#    except ValueError:
#        print("Неверный индекс :)")
#ind1=ind//10000-1
#print(uezd[ind1-1])
#if ind<=3:
#    print("Оставайтесь дома!")
#else:
#    print("Носите маски!")

#from random import *
#list=[]
#a=randint(5,14)
#for i in range(a):
#    list.append(randint(-50,50))
#print(list)
#while 1:
#    try:
#        b=int(input("Введи сколько чисел хочешь поменять: "))
#        if b<=a//2:
#            break
#    except ValueError:
#        print("Число должно быть меньше чем",a//2)
#b-=1
#for i in range(b,-1,-1):
#    print(list[i], end=" <-> ")
#    print(list[a-i-1])
#    c=list.pop(i)
#    list.insert(b-i-1-1,c)
#    c=list.pop(b-i-1)
#    list.insert(i,a)
#print(list)
#max=-50
#for element in list:
#    if element>max: max=element
#new_max=max/b
#ind=list.index(max)
#list.remove(max)
#list.insert(ind,new_max)
#print(list)
#list2=[]
#for e in list:
#    list2.append(abs(e))












