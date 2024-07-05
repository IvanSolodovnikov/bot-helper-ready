f = open('27-152b.txt', 'r')
n = int(f.readline())
print(n)
data = list(map(int, f.readlines()))
k = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if str(data[i] * data[j])[-5:] == '00000' and str(data[i] * data[j])[-6] != '0':
            k += 1
print(k)
