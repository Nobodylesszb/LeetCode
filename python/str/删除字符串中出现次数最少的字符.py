
from collections import defaultdict
while True:
    try:
        a = input()
        dd = defaultdict(int)
        for i in a:
            dd[i] += 1
            print(dd[i])
        for i in dd:
            if dd[i] == min(dd.values()):
                a = a.replace(i,'')
        print(a)
    except:
        break