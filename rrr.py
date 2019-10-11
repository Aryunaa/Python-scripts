print("Hello World hamming ")
# ключевой список(контроль)
u = []
for i in range(1, 33):
    u.append(i)

for j in range(len(u)):
    print(u[j])

print(len(u))
print(u[4] & int('100'))

# input
k = []
k = input("enter code ")

print(k)
print(len(k))

error_sindrom = []
n = len(k)
# nk=int(input("enter nk "))
nk = 4
# cори
s = []
for i in range(nk):
    s.append(k[2 ** i - 1])
print(s)

print('pochlaa!')
for i in range(nk):
    eb = 0
    o = []
    o = '0'
    print(i)  # !!!!!!!!!!!!
    sr = (2 ** i)
    print(sr)  # !!!!!!!!!!!!!!!!
    for j in range(len(k)):
        print('this is j ', j)
        # print(" ppp ")
        print('logika  ', sr & u[j])  # !!!!!!!!!!
        if (sr & u[j]) == sr:
            if k[j] == '1':
                eb += 1
        # print('new cycle j')
    print('eb %s', eb)
    if (eb % 2) != 0:
        o = '1'

    error_sindrom.append(o)
    print('this is o ', o)  #

    print('end of cycle i --------------', i)

print('end of cycle !!!')
for i in error_sindrom:
    print(i)