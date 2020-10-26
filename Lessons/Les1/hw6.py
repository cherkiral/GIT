from itertools import count, cycle
from time import sleep

for elem in cycle(count(10)):
    if elem > 100:
        break
    else:
        print(el)
        sleep(1)


for elem in cycle(input("Print something\n>")):
    print(elem)
    sleep(1)