def matrixmult(m1,m2):
    try:
        temp=[]
        temp2=[]
        # translate m2 90* counter-clockwise
        for m in range(0,len(m2[0])):
            for n in range(0,len(m2)):
                temp.append(m2[n][m])
            temp2.append(temp)
            temp=[]
        m2=temp2
        if (len(m2[0])!=len(m2[0])): return 0
        temp2=[[] for i in range(len(m2))]
        sum=0
        for yeet in range(0,len(m1)):
            for i in range(len(m2)-1,-1,-1):
                for j in range(0,len(m1[0])):
                    sum+=m1[yeet][j]*m2[i][j]
                temp2[i].append(sum)
                sum=0
        m2=temp2
        temp=[]
        temp2=[]
        # translate m2 90* counter-clockwise
        for m in range(0,len(m2[0])):
            for n in range(0,len(m2)):
                temp.append(m2[n][m])
            temp2.append(temp)
            temp=[]
        m2=temp2
        return m2
    except Exception as e:
        return 0
