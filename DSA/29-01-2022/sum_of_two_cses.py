# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IFV_MkO2Aw3Nr_UVZDQqoUn515f4JeZj
"""

n,m=input().split()
n,m=int(n),int(m)
l=list(map(int,input().split()))
dic={}
f=0
for i in range(len(l)):
    if m-l[i] in dic:
        f=1
        print(dic[m-l[i]]+1,i+1)
    dic[l[i]]=i
if f==0:
    print('IMPOSSIBLE')