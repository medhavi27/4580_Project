import pandas as pd
import numpy as np


distances=np.ndarray(shape=(11,11))

#input the number of squares along edges
#from distpatch
distances[0,1]=9
distances[0,2]=9
distances[0,3]=7
distances[0,4]=10
distances[0,5]=11
distances[0,6]=5
distances[0,7]=7
distances[0,8]=6
distances[0,9]=7
distances[0,10]=9
#from bc1
distances[1,2]=4
distances[1,3]=6
distances[1,4]=9
distances[1,5]=10
distances[1,6]=10
distances[1,7]=12
distances[1,8]=11
distances[1,9]=12
distances[1,10]=14
#from bc2
distances[2,3]=2
distances[2,4]=5
distances[2,5]=6
distances[2,6]=10
distances[2,7]=12
distances[2,8]=11
distances[2,9]=12
distances[2,10]=14
#from bc3
distances[3,4]=3
distances[3,5]=4
distances[3,6]=8
distances[3,7]=10
distances[3,8]=9
distances[3,9]=10
distances[3,10]=12
#from bc4
distances[4,5]=1
distances[4,6]=11
distances[4,7]=13
distances[4,8]=12
distances[4,9]=13
distances[4,10]=15
#from bc5
distances[5,6]=12
distances[5,7]=14
distances[5,8]=13
distances[5,9]=14
distances[5,10]=16
#from bc6
distances[6,7]=2
distances[6,8]=1
distances[6,9]=2
distances[6,10]=4
#from bc7
distances[7,8]=3
distances[7,9]=4
distances[7,10]=2
#from bc8
distances[8,9]=1
distances[8,10]=3
#from bc9
distances[9,10]=2


#distances along diagonal are 0
for i in range(11):
    distances[i,i]=0

# dist [i,j]=dist[j,i]:
for i in range(11):
    for j in range(i):
        distances[i,j]=distances[j,i]
#multiply by 5 to get distance in km and put in a dataframe
distances=pd.DataFrame(5*distances)
distances.columns=['Dis','BC_1', 'BC_2', 'BC_3', 'BC_4', 'BC_5', 'BC_6', 'BC_7', 'BC_8', 'BC_9', 'BC_10']
distances.index=['Dis','BC_1', 'BC_2', 'BC_3', 'BC_4', 'BC_5', 'BC_6', 'BC_7', 'BC_8', 'BC_9', 'BC_10']
distances
