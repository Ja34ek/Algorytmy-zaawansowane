
def Sasiedzi(G,v):
    ''' do ktorych wierzcholkow G mozna dojsc z v'''
    n=len(G)
    sasiedzi=[]
    for i in range(n):
        if G[v][i]!=0:
            sasiedzi.append(i)
    return sasiedzi


def BFS(G,v):
    ''' zwraca wierzcholki do ktorych da sie dojsc z v'''
    n=len(G)
    kolory=[0]*n
    rodzic=[None]*n
    odl=[-1]*n
    kolory[v]=1
    odl[v]=0
    Q=[]
    Q.append(v)
    while len(Q)!= 0:
        u=Q[0]
        Q.pop(0)
        for w in Sasiedzi(G,u):
            if kolory[w]==0:
                kolory[w]=1
                rodzic[w]=u
                odl[w]=odl[u]+1
                Q.append(w)
        kolory[u]=2
    wynik=[]
    for i in range(n):
        if odl[i]>-1:
            wynik.append(i)
            
        
    return wynik


def BFS_v2(G,A,B):
    '''A,B podzbiory wierzcholkow G
    zwraca sciezke z wierzcholka z A  do wierzcholka z B o ile taka istnieje''' 
    n=len(G)
    for v in A:
        kolory=[0]*n
        rodzic=[None]*n
        odl=[-1]*n
        kolory[v]=1
        odl[v]=0
        Q=[]
        Q.append(v)
        while len(Q)!= 0:
            u=Q[0]
            Q.pop(0)
            for w in Sasiedzi(G,u):
                if kolory[w]==0:
                    kolory[w]=1
                    rodzic[w]=u
                    if w in B:
                        temp=w
                        sciezka=[temp]
                        while rodzic[temp]!= None:
                            sciezka.append(rodzic[temp])
                            temp=rodzic[temp]
                        return sciezka[::-1]
                    odl[w]=odl[u]+1
                    Q.append(w)
            kolory[u]=2
        wynik=[]
        for i in range(n):
            if odl[i]>-1:
                wynik.append(i)
                   
    return print("nie istnieje")


def d(x,y):
    """
    Zwraca odleglosc euklidesowa pomiedzy punktami x i y

    """
    d=pow(x[0]-y[0],2)+pow(x[1]-y[1],2)
    return round(pow(d,1/2),1)



def Zrob_graf(S,D):
    ''' S i D to punkty na plaszczyznie [x,y] reprezentujace studnie i domy
    to ma zrobic graf dwudzielny 2*k*n wierzchoklowy (n-liczba studni n*k-liczba domow)
    '''
    n=len(S)
    nk=len(D)
    k=nk//n
    G=[]
    for i in S:
        s=[0]*(nk)
        for j in D:
            s.append(d(i,j))
        for i in range(k):
            G.append(s)
    for i in range(len(D)):
        G.append((G[i][nk:]+G[i][0:nk]))
        
    return G
            

def intersection(lst1, lst2):
    """
    Funkcja pomocnicza do wyznaczania przeciecia dwoch zbiorow
    """
    return [value for value in lst1 if (value in lst2)]


def subtraction(lst1,lst2):
    """
    Funkcja pomocnicza do wyznaczania roznicy dwoch zbiorow
    """
    return[value for value in lst1 if (value not in lst2)]


def minimum(G,y,Z):
    """
    Funkcja pomocnicza do minimum (c(i,j)-y(i)-y(j))
    """
    Stud=list(range(0,len(G)//2))
    Dom=list(range(len(G)//2,len(G)))
    ZcapS=intersection(Z,Stud)
    DminZ=subtraction(Dom,Z)
    if len(ZcapS)==0 or len(DminZ)==0:
        raise ValueError('do dupy wszystko')
    m=G[ZcapS[0]][DminZ[0]]-y[ZcapS[0]]-y[DminZ[0]]
    for i in ZcapS:
        for j in DminZ:
           
            if (G[i][j]-y[i]-y[j])<m:
                m = (G[i][j]-y[i]-y[j])
    return m
            

def update_Gy(G,y,G_y):
    """
    Uaktualnienie grafu G_y
    """
    Stud=list(range(0,len(G)//2))
    Dom=list(range(len(G)//2,len(G)))
    Gy=G_y.copy()
    for i in Stud:
        for j in Dom:
            if round(y[i]+y[j],1)==G[i][j]:
                if Gy[i][j]!=G[i][j] and Gy[j][i]!=G[i][j]:
                    Gy[i][j]=G[i][j]
            else:
                if Gy[i][j]==G[i][j] or Gy[j][i]==G[i][j]:
                    Gy[i][j]=0
                    Gy[j][i]=0           
    return Gy
                

def update_M(G_y):
    """
    Uaktualnienie pokrycia M
    """
    Gy=G_y.copy()
    M=[]
    Stud=list(range(0,len(Gy)//2))
    Dom=list(range(len(Gy)//2,len(Gy)))
    for i in Stud:
        for j in Dom:
            if Gy[j][i]>0:
                M.append([i,j])
    return M
            

def delete(L,x):
    """
    Funkcja pomocnicza
    """
    for i in range(len(L)):
        if L[i]==x:
            return L[:i]+L[i+1:]
    return L


def update_R_D(R_D,M):
    """
    Uaktualnienie zbioru R_D
    """
    RD=R_D.copy()
    for pary in M:
        if pary[1] in RD:
            RD=delete(RD,pary[1])
    if RD==None:
        return []
    return RD

def update_R_S(R_S,M):
    """
    Uaktualnienie zbioru R_S
    """
    RS=R_S.copy()
    for pary in M:
        if pary[0] in RS:
            RS=delete(RS,pary[0])
    if RS==None:
        return []
    return RS
 

def update_Z(G_y,R_D,R_S):
    """
    Uaktualnienie zbioru Z
    """
    wynik=R_S.copy()
    for v in R_S:
        temp=BFS(G_y,v)
        for w in temp:
            if w not in wynik:
                wynik.append(w)
    return wynik


def odwroc(G_y,R_S,R_D):
    """
    Odwracanie krawedzi
    """
    Gy=G_y.copy()
    sciezka=BFS_v2(Gy,R_S,R_D)
    for i in range(len(sciezka)-1):
        temp=Gy[sciezka[i]][sciezka[i+1]]
        Gy[sciezka[i]][sciezka[i+1]]=0
        Gy[sciezka[i+1]][sciezka[i]]=temp
    return Gy


def hungarian(S,D):
    """
    Glowny algorytm
    """
    n=len(S)
    k=len(D)//n
    y=[0]*(2*n*k)
    G=Zrob_graf(S,D)
    
    Stud=list(range(0,n*k))#indeksy studni
    Dom=list(range(n*k,2*n*k))# indeksy domow
    
    
    R_S=list(range(0,n*k))
    R_D=list(range(n*k,2*n*k))#wierzcholki niepokryteprzez M
    
    G_y=[]
    for i in range(2*n*k):# na poczatku w G_y nie ma zadnej krawedzi
        G_y.append([0]*(2*n*k))
        
    Z=R_S.copy()#inicjalizacja Z
    M=[]# lista par [studnia, dom]
    while len(M)<(n*k):


        if len(intersection(R_D, Z))!=0:
            G_y=odwroc(G_y,R_S,R_D)
        else:
            delta=minimum(G,y,Z)#tworzenie delty

            ZcapS=intersection(Z,range(0,n*k))
            ZcapD=intersection(Z,range(n*k,2*n*k))
            
            for i in ZcapS:#dodawanie odejmowanie delty
                y[i]+=delta
            for j in ZcapD:
                y[j]-=delta
                
            G_y=update_Gy(G,y,G_y)#dodaje ciasne i usuwam nieciasne krawedzie z Gy
            
        M=update_M(G_y)
        R_S=update_R_S(R_S,M)
        R_D=update_R_D(R_D,M)
        Z=update_Z(G_y,R_D,R_S)
    return M
    


#Ponizej dwa proste przyklady:

S=[[2,3],[1,0]]
D=[[13,3],[1,51]]

#Przyklad gdy |S|=|D|
hungarian(S,D)

S=[[-1,-1],[8,1]]
D=[[-4,4],[-1,4],[1,1],[2,4],[3,7],[3,-4]]

#Przyklad gdy |S|<|D|
hungarian(S,D)

