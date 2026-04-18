import numpy as np

# simplified to only average the np.random.random() function
active = []

while True:
    active.append(np.array([1,np.random.random()]))
    while len(active) > 1:
        if active[-1][0] == active[-2][0]:
            active.append(active.pop() + active.pop())
        else:
            break
    else:
        out = active[0]
        print(f"{int(out[0])}:\t{float(out[1] / [out[0]])}")