


def levenshtein_distance(a: str, b: str, i: int = None, j: int = None):
    if i is None:
        i = len(a)
    if j is None:
        j = len(b)
    if min(i, j) == 0:
        return max(i, j)
    return min(
        levenshtein_distance(a, b, i - 1, j) + 1,
        levenshtein_distance(a, b, i, j - 1) + 1,
        levenshtein_distance(a, b, i - 1, j - 1) + (a[i - 1] != b[j - 1])
    )



# Usage
print(levenshtein_distance("kitten", "sitting"))
print(levenshtein_distance("kitten", "kitten"))
# print(levenshtein_distance("Aodren Commun", "Aodren Conmun"))


import numpy



def printDistances(distances, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(distances[t1][t2]), end=" ")
        print()


def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    printDistances(distances, len(token1), len(token2))
    return distances[len(token1)][len(token2)]

distance = levenshteinDistanceDP("AodrenCommun", "CommunAodren")
print(distance)