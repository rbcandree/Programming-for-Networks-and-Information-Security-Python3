b_ip = input("Enter your binary ip-address, please:")
b_format = b_ip.split(".")

a = [[128, 64, 32, 16, 8, 4, 2, 1], [128, 64, 32, 16, 8, 4, 2, 1], [128, 64, 32, 16, 8, 4, 2, 1], [128, 64, 32, 16, 8, 4, 2, 1]]

c = [[], [], [], []]
for x in range(0, len(b_format)):
    for y in range(0, len(b_format[0])):
        c[x].append(int(b_format[x][y]))

d = [[], [], [], []]
for j in range(0, len(a)):
    for i in range(0, len(a[0])):
        d[j].append(a[j][i]*c[j][i])

d = [str(sum(d[num])) for num in range(0, len(d))]
ip_address = '.'.join(d)

print(f"Your ip-address of {b_ip} is: {ip_address} .")

#11101100.00010001.00001100.00001010