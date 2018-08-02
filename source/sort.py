# -*- coding: utf-8 -*-
# define functions for sort algorithm
# By yanxing

#插入排序
def insertsort(x):
    for i in range(len(x)):
        startx=0;
        endx=i;
        while startx<endx:
            j=(startx+endx)//2
            if x[i]>x[j]:
                endx=j
            else:
                startx=j+1
        y=x[i]
        for t in range(i,startx,-1):
            x[t]=x[t-1]
        x[startx]=y
    return

#冒泡排序
def bublesort(x):
    for i in range(len(x)):
        for j in range(0,len(x)-i-1):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return

#选择排序
def selectsort(x):
    for i in range(len(x)):
        t0=i
        t1=x[i]
        for j in range(i+1,len(x)):
            if x[j]<t1:
                t1=x[j]
                t0=j
        if t0!=i:
            x[t0]=x[i]
            x[i]=t1
    return

#堆排序
def heapsort(x):
    if len(x)<=0:
        return
    # 建立大根堆
    buildheap(x)
    # 建立大根堆完成
    heaplen=len(x)
    while 1:
        #提出根结点
        x[0],x[heaplen - 1] = x[heaplen - 1],x[0]
        #print(heaplen,':',x)
        heaplen -= 1
        if heaplen==0:
            break
        #将新的根结点放到合适的位置
        cnode = 0
        while 1:
            snode1 = (cnode + 1) * 2
            snode2 = snode1 - 1
            node=cnode
            maxv=x[cnode]
            if snode1 < heaplen:
                if maxv < x[snode1]:
                    maxv = x[snode1]
                    node = snode1
            if snode2 < heaplen:
                if maxv < x[snode2]:
                    maxv = x[snode2]
                    node = snode2
            #如果没有交换，就可以退出了
            if node==cnode:
                break
            x[node] = x[cnode]
            x[cnode] = maxv
            cnode = node
    return

#建立堆，ptype=1,为大根堆，ptype=2为小根堆
def buildheap(x,ptype=1):
    heaplen = len(x)
    for i in range(heaplen//2, -1, -1):
        if ptype==1:
            cnode=i
            while 1:
                snode1 = (cnode + 1) * 2
                snode2 = snode1 - 1
                node = cnode
                maxv = x[cnode]
                if snode1 < heaplen:
                    if maxv < x[snode1]:
                        maxv = x[snode1]
                        node = snode1
                if snode2 < heaplen:
                    if maxv < x[snode2]:
                        maxv = x[snode2]
                        node = snode2
                #如果没有交换，就可以退出了
                if node == cnode:
                    break
                x[node] = x[cnode]
                x[cnode] = maxv
                cnode = node
        else:
            cnode=i
            while 1:
                snode1 = (cnode + 1) * 2
                snode2 = snode1 - 1
                node = cnode
                maxv = x[cnode]
                if snode1 < heaplen:
                    if maxv < x[snode1]:
                        maxv = x[snode1]
                        node = snode1
                if snode2 < heaplen:
                    if maxv < x[snode2]:
                        maxv = x[snode2]
                        node = snode2
                if node == cnode:
                    break
                x[node] = x[cnode]
                x[cnode] = maxv
                cnode = node
    return
#快速排序, 非递归方式
def quicksort2(x,start,end):
    stack=[]
    node=[start,end]
    stack.append(node)
    #stacklen=1
    while len(stack)>0:
        #if (len(stack)>stacklen):
        #    stacklen=len(stack)
        node=stack.pop()
        start=node[0]
        end=node[1]
        if start>=end:
           continue
        key=x[start]
        i=start
        j=end
        while (i<j):
            while (i<j)&(key<x[j]):
                     j-=1
            x[i]=x[j]
            while (i<j)&(key>=x[i]):
                    i+=1
            x[j]=x[i]
        x[i]=key
        node=[start,i-1]
        stack.append(node)
        node=[i+1,end]
        stack.append(node)
    #print(stacklen)
    return

#快速排序, 递归方式
def quicksort(x,start,end):
    #print(start,end)
    if start>=end:
        return
    key=x[start]
    i=start
    j=end
    while (i<j):
        #print("1:i,j",i,j)
        while (i<j and key<x[j]):
                 j-=1
        x[i]=x[j]
        #print("2:i,j",i,j)
        while (i<j and key>=x[i]):
                i+=1
        x[j]=x[i]
    x[i]=key
    quicksort(x,start,i-1)
    quicksort(x,i+1,end)
    return

#希尔排序
def shellsort(x):
    #print("5")
    shellpass(x,5)
    shellpass(x,2)
    shellpass(x,1)
    return

def shellpass(x,d):
    xlen=len(x)
    i=0
    while i<d:
        j=i+d
        #print(i)
        while j<xlen:
            key=x[j]
            t=j-d
            while t>=i:
                if x[t]>=key:
                    x[t+d]=x[t]
                    t-=d
                else:
                    break
            x[t+d]=key
            j+=d
        i+=1
    return
