import numpy as np


def optimalStringSeparator(string, breakpoints):
    breakpoints = sorted(breakpoints)
    lenString = len(string)
    numBreakPoints = len(breakpoints)
    
    # Add to the breakpoints the first and the last indices of the string
    breakpoints = [0] + breakpoints + [lenString]
    numBreakPoints = len(breakpoints)
    breakpoints = [0] + breakpoints
    
    # Initialize the dynamic programming table
    costs = np.array([[float('inf')] * (numBreakPoints + 1) for _ in range(numBreakPoints + 1)])
    
    # Base case: cost of splitting a substring of length 0 or 1  is 0
    for i in range(1, numBreakPoints + 1):
       costs[i, i:i+2] = 0
    
    # Iterate over all possible substring lengths
    for s in range(2, numBreakPoints):
       for i in range(1, numBreakPoints - s + 1):
          j = i + s
          for k in range(i, j + 1):
             costs[i, j] = min(costs[i, j], breakpoints[j] - breakpoints[i] 
                               + costs[i, k] + costs[k, j])

    # Minimum cost of splitting the entire string into numBreakPoints + 1 sections
    return costs[1, numBreakPoints]

string = "HelloWorld"
print("Length of string:", len(string))
print("Minimum splitting cost:", optimalStringSeparator(string,[2, 9, 3]) )


