def bubble_sort(lst:list,key=lambda x: x, reverse=False):
    v=lst.copy()

    sortat=False
    while not sortat:
        sortat=True
        for i in range(len(v)-1):
            if key(v[i]) > key(v[i+1]):
                v[i], v[i+1]=v[i+1],v[i]
                sortat=False

    if reverse==False:
        return v
    else:
        return list(reversed(v))