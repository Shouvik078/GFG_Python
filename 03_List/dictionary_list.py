if __name__=='__main__':
    l1=[501,502,503]
    l2=['SDE','SMore','Konda']

d3=dict(zip(l1,l2))
print(d3)


# using for each loop

d1={l1[i]:l2[i] for i in range(len(l1))}
print(d1)


# dictionary comprehension
dic1={501: 'SDE', 502: 'SMore', 503: 'Konda'}
dic2={v:k for (k,v) in dic1.items()}
print(dic2)





