import numpy as np
N = 7 #number of nodes of graph
G = np.ones([N,N])*float("Inf")
for i in range(N):
    G[i,i] = 0 #each node with it self

#node 1
G[0,1] = 4
G[1,0] = 4
G[0,2] = 5
G[2,0] = 5
#node 2
G[1,2] = 6
G[2,1] = 6
G[1,3] = 3
G[3,1] = 3
G[1,4] = 10
G[4,1] = 10
#node 3
G[2,3] = 3
G[3,2] = 4
G[2,5] = 9
G[5,2] = 9
#node 4
G[3,4] = 4
G[4,3] = 6
G[3,5] = 3
G[5,3] = 3
#node 5
G[4,5] = 2
G[5,4] = 3
G[4,6] = 2
G[6,4] = 2
#node 6
G[5,6] = 2
G[6,5] = 2
#node 7 is linked before (last node)
#print(G)
path = np.zeros(N) #each node is conected to path value node in shortest path
D = np.zeros([N,N])
for h in range(N):
    if h==0:
        for i in range(N):
            D[h,i] = float("Inf")
        D[0,0] = 0
    else:
        D[h,0] = 0
        print("--------------In h =",h)
        for i in range(1,N):
            D[h,i] = np.min(G[i]+D[h-1])
            if np.argmin(G[i]+D[h-1]) != i: #not going through your self in min function
                path[i] = np.argmin(G[i]+D[h-1]) + 1
                if D[h,i] == float("Inf"):
                    path[i] = -1
            print("node i =",i+1, "path =",path[i], "D-hi =",D[h,i],"\\\\")
