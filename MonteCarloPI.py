import math
import random

# -1 < x(y) < 1 사이의 점들을 무작위로 만들어낸다.
def generate_point(number):
    point = []
    for i in range(number):
        x = random.uniform(-0.99999999, 1)
        y = random.uniform(-0.99999999, 1)
        point.append([x, y])
    return point

# 반지름 r보다 작은 점들만 원안에 있는 점이기 때문에 그것들만 카운트 한다.
def get_count(point):
    count = 0
    for p in point:
        x, y = p
        if math.sqrt(x**2 + y**2) < 1:
            count += 1
    return count

# 만들어진 점들과 구해진 원안의 점들로 pi를 계산한다.
def get_pi(number, count):
    return 4 * count / number

def find_pi(number):
    point = generate_point(number)
    count = get_count(point)
    return count

    

def main():
    sum = 0
    for n in range(100000, 1100000, 100000):
        c = find_pi(n)
        pi = get_pi(n, c)
        print("pi = ", pi)
        sum += pi
    average = sum / 10
    print("average = ", average)

if __name__ == "__main__":
    main()