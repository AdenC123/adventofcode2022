data = ''

with open('input.txt') as f:
    data = f.readline()


last4 = []
count = 0
for c in data:
    if len(last4) < 4:
        last4.append(c)
    elif len(set(last4)) == 4:
        print(count)
        break
    else:
        last4 = last4[1:]
        last4.append(c)
    count += 1


