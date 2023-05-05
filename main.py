from claseconjunto import Conjunto


if __name__ == '__main__':
    A = Conjunto([1,2,3,4])
    B = Conjunto([3,6,9])
    C = A.__ad__(B)
    D = A.__sub__(B)

    print(f"A = {A}")
    print(f"B = {B}")
    print(C)
    print(D)
    print(A == Conjunto([1,2,3,4]))