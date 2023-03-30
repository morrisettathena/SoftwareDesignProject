import numpy as np

f = open("COMSC110S20.SEC","r")
bruh = f.read()
bruh = bruh.replace(","," ")
bruh = bruh.replace("\"", "")
with open(r'COMSC110S20.SEC', 'w') as file:
    file.write(bruh)
bruh2 = np.loadtxt("COMSC110S20.SEC", skiprows=1,dtype='str')
