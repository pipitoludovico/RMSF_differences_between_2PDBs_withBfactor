import sys
import os

sys1 = sys.argv[1]
sys2 = sys.argv[2]

indict = [sys1, sys2]

for i in indict:
    os.system("sed -i 's/HSP/HIS/g' %s" % i)
    os.system("sed -i 's/HSE/HIS/g' %s" % i)
    os.system("sed -i 's/HSD/HIS/g' %s" % i)

d = {}

with open(sys1, "r") as f:
    for line in f:
        identifier = str(line.split()[3] + " " + line.split()[5])

        if identifier not in d:
            d[identifier] = round(float(line.split()[-1]), 2)

dd = {}

with open(sys2, "r") as f:
    for line in f:
        identifier2 = str(line.split()[3] + " " + line.split()[5])

        if identifier2 not in dd:
            dd[identifier2] = round(float(line.split()[-1]), 2)

for key, value in dd.items():
    for k, v in d.items():
        if key == k:
            dd[key] = round(float(dd[key] - d[key]), 2)

sys2_cont = open('difference.pdb', 'w')
with open(sys1, "r") as template:
    for line in template:
        if line.split()[3] + " " + line.split()[5] in dd:
            b_value = dd[line.split()[3] + " " + line.split()[5]]
            b_value = round(b_value, 2)
            l_second_part = str(b_value)
            sys2_cont.write(line[0:62] + l_second_part + '\n')
            continue
        sys2_cont.write(line)
    sys2_cont.close()
