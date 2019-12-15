def linearsolve(eq):
    temp=eq.split(' ')
    temp=''.join(temp)
    inds= [[i for i in temp].index('*'),[i for i in temp].index('+'),[i for i in temp].index('=')]
    cops=[temp for i in range(len(inds))]
    for i in range(0,len(cops)):
        cops[i]=[j for j in cops[i]]
    for i in range(0,len(cops)):

        cops[i]=cops[i][0:inds[i]]
    cops=[cops[0],cops[-1]]
    inds=cops[-1].index('+')
    cops[-1]=cops[-1][inds+1:]
    cops=[float(''.join(i)) for i in cops]
    cops=-cops[-1]/cops[0]
    return cops
