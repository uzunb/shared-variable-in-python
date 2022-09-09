
from Fruit import Fruit

def main():
    print("main    : " + str(Fruit.count))
    print("main-id : " + str(id(Fruit.count)))

    Fruit.count = 5

    import call1

if __name__ == '__main__':
    main()