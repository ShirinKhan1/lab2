from faker import Faker
from random import randint
import numpy as np

fake = Faker()
M, N = 10, 3
rules = {
    "Полный запрет": bin(0)[2:],
    "Передача прав": bin(1)[2:],
    "Запись": bin(2)[2:],
    "Запись, Передача прав": bin(3)[2:],
    "Чтение": bin(4)[2:],
    "Чтение, Передача прав": bin(5)[2:],
    "Чтение, запись": bin(6)[2:],
    "Полный доступ": bin(7)[2:]

}
bd = np.full((M, N), 0)
bd.astype('str')
names = {}
if __name__ == "__main__":
    for i in range(M):
        for j in range(N):
            bd[i][j] = bin(randint(0, 7))[2:]

        names[fake.name()] = bd[i]

    for key, value in names.items():
        print("{0}:\t{1}".format(key, value))

    while True:
        name = input("Введи индетификатор - ")
        if not (names.get(name) is None):
            print(
                f"0	000	Полный запрет"
                f"\n1	001	Передача прав"
                f"\n2	010	Запись"
                f"\n3	011	Запись, Передача прав	"
                f"\n4	100	Чтение	"
                f"\n5	101	Чтение, Передача прав	"
                f"\n6	110	Чтение, Запись	"
                f"\n7	111	Полный доступ	"
            )
            print(names[name])
            command = rules.get(input("Жду ваших указаний > "))
            while True:
                if command is None:
                    command = rules.get(input("Жду ваших указаний > "))
                else:
                    obt = int(input("Над каким объектом производится операция? ")) - 1
                    while True:
                        if obt in range(N):
                            break
                        else:
                            obt = int(input("Над каким объектом производится операция? ")) - 1


