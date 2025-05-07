import numpy as np

def calculate_splitting_cost(prices, num_parts):
    
  prices = [0] + prices + [num_parts]
  m = len(prices)
  prices = [0] + prices
  costs = np.full((m + 1, m + 1), np.inf)
  #print(costs)
  for i in range(1, m + 1):
     costs[i, i:i+2] = 0
     print(costs)

  for s in range(2, m):
     for i in range(1, m - s + 1):
        j = i + s
        for k in range(i, j + 1):
           costs[i, j] = min(costs[i, j], prices[j] - prices[i] + costs[i, k] + costs[k, j])

  return costs[1, m]


string = "abcdfedghjg"
print("Length of string:", len(string))
print("Minimum splitting cost:", calculate_splitting_cost([1, 6, 3],len(string)))


# def splitString(Y, n):
#     '''
#        Split the string at locations specified in M
#         Arguements: 
#             Y = list of numbmers where cut shuld take place. Integer.
#             n = Number of characers in string. Integer.
#         Returns Minimum Cost CutList.   

#         M stores the minimum cost of splitinng the string 
#     '''
#     m = len(Y)
#     Y.sort()
#     n = 20
    
#     M = np.array([[np.inf for x in range(m+2)] for x in range (m+2)])
  
 
#     newY = [-1 for x in range(m+2)]
#     newY[0] = 0
#     for i in range(m):
#         newY[i+1] = Y[i]
#     newY[m+1] = n

#     for i in range(m+2):
#         M[i,i] = 0
    
#     for i in range(m+1):
#         M[i,i+1] = 0
    
#     for incr in range(2, m+2):
#         for i in range(m+2-incr):
#             j = i + incr
#             minCost = np.inf
#             firstCut = abs(newY[j] - newY[i])

#             for l in range(i+1, j):
#                 print("(incr,i+1, j, l)=({},{},{},{}), newY[j]={}, newY[i]={}".format(incr, i+1, j, l, newY[j], newY[i+1]))
#                 cost = M[i,l] + M[l,j] #+ abs(newY[j] - newY[i+1])
#                 if(cost < minCost):
#                     minCost = cost 
#             if(minCost == np.inf):
#                 minCost = firstCut
#             else:
#                 minCost = minCost + firstCut
#             M[i,j] = minCost
    
#     print(M)
#     print("Min cost is ",  M[0,m+1]) 
#     return



# string = "abcdfedghjg"
# print("Length of string:", len(string))
# print("Minimum splitting cost:", splitString([1, 6, 3],len(string)))