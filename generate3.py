#from lammps import lammps
from itertools import product
from random import sample
from pathlib import Path
import shutil
import numpy as np
# Ids of the carbon and calcium atoms respectively which are going to be removed
co_ids = [65, 67, 145, 147, 225, 227, 305, 307, 385, 387, 465, 467, 545, 547, 625, 627, 705, 707, 785, 787, 865, 867, 945, 947, 1025, 1027, 1105, 1107, 1185, 1187, 1265, 1267, 1345, 1347, 1425, 1427]
ca_ids = [61, 63, 141, 143, 221, 223, 301, 303, 381, 383, 461, 463, 541, 543, 621, 623, 701, 703, 781, 783, 861, 863, 941, 943, 1021, 1023, 1101, 1103, 1181, 1183, 1261, 1263, 1341, 1343, 1421, 1423]
# cob_ids = [24, 28, 114, 118, 204, 208, 294, 298, 384, 388, 474, 478]
# cab_ids = [7, 12, 97, 102, 187, 192, 277, 282, 367, 372, 457, 462]
# Combine the ids and generate all possible pairs C-Ca
ids = co_ids + ca_ids
comb_ids = list(product(co_ids,ca_ids))
folders=range(len(comb_ids))

open_template=open("defect_template.lmp", "r")
template=open_template.read()

open_template2=open("run_template.lmp")
template2=open_template2.read()

open_template3=open("jobs_template.sh")
template3=open_template3.read()
# For each pair, id1 will replace a carbon id and id2 will replace a calcium id in in.lammps file
#
# print(template)
for item,folder in zip(comb_ids,folders):
    data = {'co': item[0], 'ca': item[1], 'foldername':folder}
    print ('co is %(co)s and Ca is %(ca)s' % data)
    # Read in the file
    # with open('in.lmp', 'r') as file :
    #     filedata = file.read()
    # filedata = filedata.replace('id1','{}'.format(item[0]))
    # filedata = filedata.replace('id2','{}'.format(item[1]))
    with open('defect.lmp', 'w') as file:
        file.write(template % data)
    with open('in.lmp', 'w') as file:
        file.write(template2 % data)
    p = Path('arg_%(foldername)s' %  data)
    p.mkdir(exist_ok=True)
    shutil.move("in.lmp", "arg_%(foldername)s" % data)
    shutil.move("defect.lmp", "arg_%(foldername)s" % data)
    shutil.copy("new.data", "arg_%(foldername)s" % data)
    shutil.copy("seed.sh", "arg_%(foldername)s" % data)
#    shutil.copy("job.sh", "vtr_%(foldername)s" % data)

#jstart,jstop=[range(0,72,18),range(18,73,18)]
jstart,jstop=[range(0,1296,9),range(8,1297,9)]

for start,stop in zip(jstart,jstop):
    data={'jstart':start,'jstop':stop}
    with open('job_%(jstart)s_%(jstop)s.sh' % data, 'w') as file:
        file.write(template3 % data)
