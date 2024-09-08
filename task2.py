from math import sqrt

if __name__ == '__main__':
#             # C:\Users\User\Desktop\Krug.txt
            
#             # C:\Users\User\Desktop\Tochka.txt
    path1 = input('Путь до файла с координатами и радиусом окружности: ')
    path2 = input('Путь до файла с координатами точек: ')
    
    with open(path1) as f:
        xc, yc = map(float, f.readline().split())
        r = int(f.readline().strip())
    
    with open(path2) as f:
        points = [list(map(float, line.strip().split())) for line in f]
    
    for x, y in points:
        s = sqrt((xc - x) ** 2 + (yc - y) ** 2)
        if s == r:
            print(0)
        elif s < r:
            print(1)
        else:
            print(2)
