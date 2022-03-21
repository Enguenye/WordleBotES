import pandas as pd
import numpy as np
import math
import logging
import threading
import time
import multiprocessing



def thread_function(list2,complete):
    finalword = ""
    maxEntropy = 0
    for word in list2:
        if word != False:
            arr = list(word)
            listSum = []
            for i1 in range(3):
                for i2 in range(3):
                    for i3 in range(3):
                        for i4 in range(3):
                            for i5 in range(3):
                                arrtemp = complete
                                index = 0
                                toRemove = []
                                for word2 in arrtemp:
                                    if(word2==False):
                                        toRemove.append(index)
                                    elif (i1 == 0 and arr[0] in word2):
                                        toRemove.append(index)
                                    elif (i1 == 1 and (word2[0] not in arr or word2[0]==arr[0])):
                                        toRemove.append(index)
                                    elif (i1 == 2 and (word2[0] != arr[0])):
                                        toRemove.append(index)
                                    elif (i2 == 0 and arr[1] in word2):
                                        toRemove.append(index)
                                    elif (i2 == 1 and (word2[1] not in arr or word2[1]==arr[1])):
                                        toRemove.append(index)
                                    elif (i2 == 2 and (word2[1] != arr[1])):
                                        toRemove.append(index)
                                    elif (i3 == 0 and arr[2] in word2):
                                        toRemove.append(index)
                                    elif (i3 == 1 and (word2[2] not in arr or word2[2]==arr[2])):
                                        toRemove.append(index)
                                    elif (i3 == 2 and (word2[2] != arr[2])):
                                        toRemove.append(index)
                                    elif (i4 == 0 and arr[3] in word2):
                                        toRemove.append(index)
                                    elif (i4 == 1 and (word2[3] not in arr or word2[3]==arr[3])):
                                        toRemove.append(index)
                                    elif (i4 == 2 and (word2[3] != arr[3])):
                                        toRemove.append(index)
                                    elif (i5 == 0 and arr[4] in word2):
                                        toRemove.append(index)
                                    elif (i5 == 1 and (word2[4] not in arr or word2[4]==arr[4])):
                                        toRemove.append(index)
                                    elif (i5 == 2 and (word2[4] != arr[4])):
                                        toRemove.append(index)
                                    index += 1
                                arrtemp = np.delete(arrtemp, toRemove)
                                p = (len(arrtemp) / len(list2))
                                sum = 0
                                if (p != 0):
                                    sum = p * math.log(1 / p, 2)
                                listSum.append(sum)
            entropy = np.sum(listSum)
            print(word)
            if (entropy >= maxEntropy):
                maxEntropy = entropy
                finalword = word
    print("la palabra con mayor entropia es " + finalword)



df = pd.read_excel('./Lista5Palabrasespa.xlsx')
list2 = df["LIST"].to_numpy()
complete=list2

defList=np.array_split(list2, 6)

t1=threading.Thread(target=thread_function, args=(defList[0],complete))
t1.start()

t2=threading.Thread(target=thread_function, args=(defList[1],complete))
t2.start()

t3=threading.Thread(target=thread_function, args=(defList[2],complete))
t3.start()

t4=threading.Thread(target=thread_function, args=(defList[3],complete))
t4.start()

t5=threading.Thread(target=thread_function, args=(defList[4],complete))
t5.start()

t6=threading.Thread(target=thread_function, args=(defList[5],complete))
t6.start()

