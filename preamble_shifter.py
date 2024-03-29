import numpy as np

shifting = 160

dataset = []

fname = " "
for fname in ["/home/leehyunjong/Wi-Fi_Preambles/"
              "WIFI_10MHz_IQvector_6dB_20000.txt"]:

    print(fname)
    f = open(fname, "r", encoding='utf-8-sig')
    linedata = []

    for line in f:
        if line[0] == "#":
            continue

        linedata = [x for x in line.split()]
        if len(linedata) == 0:
            continue

        dataset.append(linedata)

    f.close()

dataset = np.array(dataset)

dataset[0:10000, 0:shifting] = dataset[10000:20000, 0:shifting]

fname = str(shifting) + "_Shifted_WIFI_10MHz_IQvector_6dB_20000.txt"

np.savetxt(fname, dataset, fmt='%s', delimiter=' ')
