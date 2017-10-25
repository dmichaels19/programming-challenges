from pprint import pprint
import math

X = [0, -60, -62, -60, 63, -97]
Y = [-72, 67, 61, -8, -32, 89]
R = [6, 7, 8, 7, 5, 6]
Z = 918

class RadioRange:
    def RadiusProbability(X, Y, R, Z):
        intervals = [(math.sqrt(x**2+y**2)-r,math.sqrt(x**2+y**2)+r) for x,y,r
                        in zip(X,Y,R)]
        intervals.sort()

        # start running unions
        unions = []
        union = (0,0)

        for interval in intervals:
            #useless if outside [0,Z]
            if interval[0] >= Z:
                break
            if not (union[1] < interval[0]) and not (interval[1] < union[0]):
                union = (union[0],max(union[1],interval[1]))
            else:
                unions.append(union)
                union = interval
        if not unions or unions[-1] != union:
            unions.append(union)

        # sum lengths of bad radius areas
        count = sum(j - i for i,j in unions)

        # probability is valid territory length divided by [0,Z]
        return (Z - count) / Z


radio = RadioRange.RadiusProbability(X,Y,R,Z)
print (radio)
