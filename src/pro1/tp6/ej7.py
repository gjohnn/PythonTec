import random
chars=[]

while len(chars)<51:
    chars.append(chr(random.randrange(97, 123)))


qty_foreach_char = []
for e in chars:
    count = chars.count(e)
    if (e, count) in qty_foreach_char:
        continue
    tuple_char = (e,count)
    qty_foreach_char.append(tuple_char)

for element in qty_foreach_char:
    print(element)
