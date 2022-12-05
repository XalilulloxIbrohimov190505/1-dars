import random
import time
qatnashchilar = int(input("Qatnashchilar sonini kirit:"))
royxat = []
for i in range(qatnashchilar):
    royxat.append(input(f"{i+1}-Ishtirokchini kirit:").capitalize())

while len(royxat) != 1:
    if len(royxat)>2:
        royxat.remove(random.choice(royxat))
        random.shuffle(royxat)
        time.sleep(3)
        print(royxat)
    if len(royxat) == 2:
        royxat.remove(random.choice(royxat))
        random.shuffle(royxat)
        time.sleep(10)
        print(royxat)
print(f'Tabriklaymiz!!!{(royxat[0]).upper()} g`olib bo`ldi')
