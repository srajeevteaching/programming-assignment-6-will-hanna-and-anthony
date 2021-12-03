# Programmers: Anthony, Will, Hanna
# Course: CS151, Dr. Rajeev
# Programming Assignment: 6
# Program Inputs: File name
# Program Ouputs: Difference of likes and shares, average likes per type of post
import numpy as np
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
    idk=[['Photo',0,0],['Link',0,0],['Video',0,0],['Status',0,0]]
    for i in fb:
        for x in idk:
            if i[1]==x[0]:
                x[1]+=1
                x[2]+=float(i[16])
    for i in idk:
        i[1]= i[2]/i[1]
    for i in idk:
        i.pop()
        i[1]=round(i[1],2)
    print(idk)


def main():
    Facebook_List=read_file('facebook.csv')
    x=input("what would you like the filename to be?")
    filename=str(x)+'.txt'
    out=difference(Facebook_List)
    filemaker(out,filename)
    type_likes(Facebook_List)


main()
