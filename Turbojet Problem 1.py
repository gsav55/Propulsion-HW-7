#Turbojet Engine

import math
import matplotlib.pyplot as plt
import numpy as np

# Conditions given in the problem
Pa = 12.112
Ta = 216.65
To4_max
gamma1 = 1.4
gamma2 = 1.3
R = 287
Cp1 = 1.0045
Cp2 = 1.24367
M=1.8
Fst=0.06
hc=43124

#Efficiencies
nd=0.9
nc=0.9
nb=0.98
rb=0.97
nt=0.92
nn=0.98
 

Mlist = np.array([])
Ilist = np.array([])
TSFClist = np.array([])
nthlist = np.array([])
nplist = np.array([])
nolist = np.array([])
rclist = np.array([])
A_ratiolist = np.array([])

#Flow Conditions
Toa = Ta*(1 + ((gamma1-1)/2)*M**2)
print Toa
Poa = Pa*(1 + ((gamma1-1)/2)*M**2)**(gamma1/(gamma1-1))
print Poa
u_in = M*math.sqrt(gamma1*R*Ta) 
print u_in

#Inlet/Diffuser
To2=Toa
To2s=nd*(To2-Ta)-Ta
print To2s
Po2=Pa*(To2s/Ta)**(gamma1/(gamma1-1))
print Po2

#Compressor
for rc in np.arange(2,60,0.1):
    To4 = To4_max
    
    To3s=To2*rc**((gamma1-1)/gamma1)
	if rc == 2:
		print To3s
	Po3=rc*Po2
	if rc == 2:
		print Po3
	To3 = ((To3s-To2)/nc)+To2
	if rc == 2:
		print To3
	wc_in = Cp1*(To3-To2)
	if rc == 2:
		print wc_in
	
	#Combustor
	Fb=(((To4/To3)-1)/((nb*hc/(Cp2*To3))-(To4/To3)))
	if Fb >= Fst:
		Fb = Fst
		To4 = (Fb*nb*hc/(Cp2)+Toa)/(1+Fb)
	Po4=Po3
	
	#Turbine
	wt_out=wc_in
	To5=To4-(wt_out/(cp*(1+Fb)))
	if rc == 2:
		print To5
	To5s=To4-((To4-To5)/nt)
	if rc == 2:
		print To5s
	Po5=Po4*(To5s/To4)**(gamma2/gamma2-1)
	if rc == 2:
		print Po5
	
	#Nozzle
	To6=To5
	To7=To6
	Po6=Po5
	P7=Pa
	T7as=(To6/((Po6/P7)**(gamma2-1/gamma2)))
	if rc == 2:
		print T7as
	T7=To6-nn*(To6-T7as)
	if rc == 2:
		print T7
	M7=math.sqrt(((To7/T7)-1)*(2/(gamma2-1)))
	if rc == 2:
		print M7
	u7 = M7*math.sqrt(gamma2*R*T7)
	if rc == 2:
		print u7
		
    I = (1+Fb)*u7-u_in
    TSFC = Fb/I
	nth=(((1+Fb)*u7**2-u_in**2)/(2*Fb*hc*1000))
	np=(2*u_in/(u7+u_in))
	no=nth*no
	A_ratio = (1/M7)*((2/2.3)*(1+(0.3/2)*M7**2))**(2.3/0.6)
	
    Ilist=np.append(Ilist,I)
    TSFClist=np.append(TSFClist,TSFC)
    A_ratiolist=np.append(A_ratiolist,A_ratio) 
	nthlist=np.append(nthlist,nth)
	nplist=np.append(nplist,np)
	nolist=np.append(nolist,no)
	rclist=np.append(rclist,rc)
	
    
# Now to plot everything!
plt.figure(1)
plt.plot(rclist, Ilist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Specific Thrust, I')
plt.title('I vs r_c')

plt.figure(2)
plt.plot(rclist, TSFClist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('TSFC')
plt.title('TSFC vs r_c')

plt.figure(3)
plt.plot(rclist, nthlist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Thermal Efficiency, nth')
plt.title('Thermal Efficiency vs r_c')

plt.figure(4)
plt.plot(rclist, nplist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Propulsive Efficiency, np')
plt.title('Propulsive Efficiency vs r_c')

plt.figure(5)
plt.plot(rclist, nolist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Overall Efficiency, no')
plt.title('Overall Efficiency vs r_c')

plt.figure(6)
plt.plot(rclist, A_ratiolist)
plt.xlabel('Compressor Pressure Ratio, r_c')
plt.ylabel('Area Ratio, A/A*')
plt.title('Area Ratio vs r_c')

plt.show()