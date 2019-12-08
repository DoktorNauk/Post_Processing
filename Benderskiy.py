
from latexlate.Template import Template

import sys, io,os
parametrs=['MV','P','P_tot','T','T_tot','Mach']
Xi=[0.99, 1.49, 1.51, 2.5, 3.5, 4.49, 4.51, 4.99, 5.99]
latpars=['MV','P','P_{tot}','T','T_{tot}','Mach']
 
Ways1=[]
Ways2=[]
Param=[]
X=[]
lp=[]
j=0
for p in parametrs:
    for x in Xi:
        c=str(int(100*x))
        Ways1.append(f'Mesh1/Images/{p}_X={c}')
        Ways2.append(f'Mesh2/Images/{p}_X={c}')
        Param.append(p)
        X.append(x)
        lp.append(latpars[j])
    j=j+1

 

























x=1













with io.open(sys.argv[1], 'r', encoding="utf-8") as file:
    text = ''.join(file.readlines())
t = Template(text, globals())
out = t.render()

with io.open(sys.argv[2], 'w', encoding="utf-8") as file:
    file.write(out)

