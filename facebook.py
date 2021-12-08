# Programmers: Anthony, Will, Hanna
# Course: CS151, Dr. Rajeev
# Programming Assignment: 6
# Program Inputs: File name
# Program Ouputs: Difference of likes and shares, average likes per type of post
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
def read_file(filename):
    data_list=[]
    file=open(filename,"r")
    for line in file:
        data_list.append(line.split(";"))
    file.close()
    return data_list
def fixlast(l):
    for x in l:
        x[-1] = x[-1].strip()
    return l
def filemaker(l,filename):
    t=open(filename,'w')
    for x in l:
        t.write(str(x)+"\n")
def difference(fb):
    out=[]
    for i in fb:
        if float(i[16])>float(i[17]):
            diff=float(i[16])-float(i[17])
            los='likes'
        else:
            diff=float(i[17])>float(i[16])
            los='share'
        if diff <= 25:
            change='no change'
        elif diff <= 100:
            change='more'
        else:
            change='significantly more'
        a=[i[1],los,change]
        out.append(a)
    return out
def type_likes(fb):
    b=[['Photo',0,0],['Link',0,0],['Video',0,0],['Status',0,0]]
    for i in fb:
        for x in b:
            if i[1]==x[0]:
                x[1]+=1#times it happens
                x[2]+=float(i[16])#total likes
    for i in b:
        i[1]= i[2]/i[1]
    for i in b:
        i.pop()
        i[1]=round(i[1],2)
    print("The average likes for each type are...")
    print(b)

def make_list(fb):
    a=[0,0,0]
    for i in fb:
        if float(i[9])<100:
            a[0]+=1
        if float(i[9])<400:
            a[1]+=1
        else:
            a[2]+=1
    return a
def month_engage(m,fb):
    x=[0]*12
    val=0
    c=0
    for i in fb:
        x[int((float(i[3])-1))]+=1
    for i in x:
        if i > val:
            val=i
            num=c
        c+=1
    print('The month with the highest engagement is...')
    print(m.get(str(num)))



def makegraph(a):
    Sections=['Low','Medium','High']
    xpos = np.arange(len(Sections))
    plt.xticks(xpos,Sections)
    plt.bar(xpos,a)
    plt.title('Posts with Low, Medium and High Engagements ')
    plt.ylabel('Number of Engagements')

    plt.tight_layout()

    plt.show()


def main():
    month = {'1': 'Janauary',
             '2': 'February',
             '3': 'March',
             '4': 'April',
             '5': 'May',
             '6': 'June',
             '7': 'July',
             '8': 'August',
             '9': 'September',
             '10': 'October',
             '11': 'November',
             '12': 'December'	}
    Facebook_List=read_file('facebook.csv')
    x=input("what would you like the filename to be?")
    filename=str(x)+'.txt'
    out=difference(Facebook_List)
    filemaker(out,filename)
    type_likes(Facebook_List)
    dalist=make_list(Facebook_List)
    month_engage(month, Facebook_List)
    makegraph(dalist)


main()
