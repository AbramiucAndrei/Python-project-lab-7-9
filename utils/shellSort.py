def shell_sort(lst, key=lambda x: x, reverse=False):
    v=lst.copy()

    gap=len(lst)//2
    while(gap>0):
        for i in range(gap,len(v)):
            aux=v[i]

            poz=i
            while(poz-gap>=0 and key(v[poz-gap])>key(aux)):
                v[poz]=v[poz-gap]
                poz-=gap

            v[poz]=aux

        gap=gap//2

    if reverse == True:
        return list(reversed(v))
    else:
        return v
