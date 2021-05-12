def pangkat(x, n):
    if n == 0:
        return 1
    else:
        result = x * pangkat(x, n - 1)
        return result


tulis = "Masukan bilangan yg dipangkatkan = "
y = int(input(tulis))
tulisan = "Masukan bil perpangkatanya = "
m = int(input(tulisan))
print(y, "Pangkat",m, "=",pangkat(y,m))
