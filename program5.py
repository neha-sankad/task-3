import operator
def most_frequent(string):
    d={}
    for i in s:
        count=0
        for j in s:
            if i==j:
                count+=1
                d[i]=count
    return d
s=input("enter the string: ")
dict=most_frequent(s)
sorted_d =(sorted(dict.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)

