import re
import matplotlib.pyplot as plt
import skrf as rf

MEAS_1 = r'MEAS_COAX_FEED_HORN_#1.s1p'
MEAS_2 = r'MEAS_COAX_FEED_HORN_#2.s1p'
MEAS_3 = r'MEAS_COAX_FEED_HORN_#3.s1p'
MEAS_4 = r'MEAS_COAX_FEED_HORN_#4.s1p'
SIM = r'SIM_COAX_FEED_HORN.s1p'

for file in [MEAS_1, MEAS_2,MEAS_3,MEAS_4,SIM]:
    with open(file, encoding='cp1252') as f:
        for line in f:
            print(line.rstrip())
            if re.search('#', line):
                break
            else:
                pass
    print('\n')

sedat_1 = rf.Network(MEAS_1)
sedat_2 = rf.Network(MEAS_2)
sedat_3 = rf.Network(MEAS_3)
sedat_4 = rf.Network(MEAS_4)
sedat_6 = rf.Network(SIM)


sedat_1.plot_s_db(m=0,n=0) #S11
sedat_2.plot_s_db(m=0,n=0) #S11
sedat_3.plot_s_db(m=0,n=0) #S11
sedat_4.plot_s_db(m=0,n=0) #S11
sedat_6.plot_s_db(m=0,n=0,linestyle = '--',linewidth = 3) #S11

plt.minorticks_on()
plt.grid(visible=True, which='major', color='black', linestyle='-')
plt.grid(visible=True, which='minor', color='grey', linestyle='--')
plt.show()


sedat_1.plot_s_smith(m=0,n=0) #S11
sedat_2.plot_s_smith(m=0,n=0) #S11
sedat_3.plot_s_smith(m=0,n=0) #S11
sedat_4.plot_s_smith(m=0,n=0) #S11
sedat_6.plot_s_smith(m=0,n=0,linestyle = '--',linewidth = 3) #S11

plt.minorticks_on()
plt.grid(visible=True, which='major', color='black', linestyle='-')
plt.grid(visible=True, which='minor', color='grey', linestyle='--')
plt.show()



