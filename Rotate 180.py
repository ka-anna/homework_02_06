#Write a program that rotates a matrix by 180 degrees.

m = list(range(1,17))
for i in range(0,16,4):
    print(m[i:i+4])
m.reverse()
for i in range(0,16,4):
    print(m[i:i+4])
