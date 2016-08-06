# Project Euler
# Problem 191 - 35%

#Tribonacci numbers
#0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, ...

serie=[0,0,1]

def trib(n):
    if n > len(serie)-1:
        serie.append( trib(n-1) + trib(n-2) + trib(n-3) )
    return serie[n]

def calc(n):
  return sum( [ trib(i-1+3) * trib(n-i+3) for i in range(n+1) ] )


print calc(4)
print calc(30)

