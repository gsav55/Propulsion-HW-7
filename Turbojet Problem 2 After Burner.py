#Turbojet Engine Problem 2

import math
import matplotlib.pyplot as plt
import numpy as np

# Conditions given in the problem
Pa = 12.112
Ta = 216.65
To4_max = 1500
gamma1 = 1.4
gamma2 = 1.3
R = 287
Cp1 = 1.0045
Cp2 = 1.24367
M=1.8
Fst=0.06
hc=43124
To6_max = 2000

#Efficiencies
nd=0.9
nc=0.9
nb=0.98
rb=0.97
nt=0.92
nn=0.98
nab=0.95
rab=0.97
 

Mlist = []
Ilist = []
TSFClist = []
nthlist = []
nplist = []
nolist = []
rclist = []
A_ratiolist = []

#Flow Conditions
Toa = Ta*(1 + ((gamma1-1)/2)*M**2)
print Toa
Poa = Pa*(1 + ((gamma1-1)/2)*M**2)**(gamma1/(gamma1-1))
print Poa
u_in = M*math.sqrt(gamma1*R*Ta) 
print u_in

#Inlet/Diffuser
To2=Toa
To2s=nd*(To2-Ta)+Ta
print 'To2s '
print 'To2s '
Po2=Pa*(To2s/Ta)**(gamma1/(gamma1-1))
print 'Po2 '
print Po2

#Compressor
for rc in np.arange(2,60,0.1):
    To4 = To4_max
    
    To3s=To2*rc**((gamma1-1)/gamma1)
    if rc == 2:
        print 'To3s '
        print To3s
    Po3=rc*Po2
    if rc == 2:
        print 'Po3 '
        print Po3
    To3 = ((To3s-To2)/nc)+To2
    if rc == 2:
    	print 'To3 '
    	print To3
    wc_in = Cp1*(To3-To2)
    if rc == 2:
        print 'wc_in '
        print wc_in
	
    #Combustor
    Fb=(((To4/To3)-1)/((nb*hc/(Cp2*To3))-(To4/To3)))
    if Fb >= Fst:
    	Fb = Fst
    	To4 = (Fb*nb*hc/(Cp2)+Toa)/(1+Fb)
    Po4=rc*Po2
    if rc == 2:
        print 'Fb '
        print Fb
	
    #Turbine
    wt_out=wc_in
    To5=To4-(wt_out/(Cp2*(1+Fb)))
    if rc == 2:
        print 'To5 '
        print To5
    To5s=To4-((To4-To5)/nt)
    if rc == 2:
        print 'To5s '
        print To5s
    Po5=Po4*(To5s/To4)**(gamma2/gamma2-1)
    if rc == 2:
    	print 'Po5 '
    	print Po5

    #Afterburner
    Po6A=rab*Po5
    To6A = To6_max
    Fab=((1+Fb)*(To6A-To5))/((nab*hc/Cp2)-To6A)
    if Fab+Fb >= Fst:
    	Fab = Fst-Fb
    	To6A = (To5*(1+Fb))/(Fab+Fb+1)
        
    #Nozzle
    To7A=To6A
    P7A=Pa
    T7As=(To6A/((Po6A/P7A)**(gamma2-1/gamma2)))
    if rc == 2:
    	print 'T7As '
    	print T7As
    T7A=To6A-nn*(To6A-T7As)
    if rc == 2:
    	print 'T7A '
    	print T7A
    M7A=math.sqrt(((To7A/T7A)-1)*(2/(gamma2-1)))
    if rc == 2:
    	print 'M7A '
    	print M7A
    u7A = M7A*math.sqrt(gamma2*R*T7A)
    if rc == 2:
        print 'u7A '
        print u7A
		
    I = (1+Fb+Fab)*u7A-u_in
    TSFC = Fb/I
    nth=(((1+Fb+Fab)*u7A**2-u_in**2)/(2*(Fab+Fb)*hc*1000))
    np=(2*u_in/(u7A+u_in))
    no=nth*np
    A_ratio = (1/M7A)*((2/2.3)*(1+(0.3/2)*M7A**2))**(2.3/0.6)
	
    Ilist.append([I])
    TSFClist.append([TSFC])
    A_ratiolist.append([A_ratio])
    nthlist.append([nth])
    nplist.append([np])
    nolist.append([no])
    rclist.append([rc])
	
    
# Now to plot everything!
plt.figure(1)
plt.plot(rclist, Ilist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Specific Thrust, I')
plt.title('After Burner I vs r_c')

plt.figure(2)
plt.plot(rclist, TSFClist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('TSFC')
plt.title('After Burner TSFC vs r_c')

plt.figure(3)
plt.plot(rclist, nthlist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Thermal Efficiency, nth')
plt.title('After Burner Thermal Efficiency vs r_c')

plt.figure(4)
plt.plot(rclist, nplist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Propulsive Efficiency, np')
plt.title('After Burner Propulsive Efficiency vs r_c')

plt.figure(5)
plt.plot(rclist, nolist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Overall Efficiency, no')
plt.title('After Burner Overall Efficiency vs r_c')

plt.figure(6)
plt.plot(rclist, A_ratiolist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Area Ratio, A/A*')
plt.title('After Burner Area Ratio vs r_c')

plt.show()
