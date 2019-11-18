# CE340: Automation Control Systems
#
#   Evangelos Stamos
#   02338
#   estamos@e-ce.uth.gr
#
#
#_______________________________________________________________________________
#   Alpha   : 31-10-19
#   Beta    : 01-11-19
#   Stable  : 04-14-19
#   Final   : 11-11-19
#_______________________________________________________________________________

# Import libraries
import numpy as np
import control.matlab as mtlb
import matplotlib.pyplot as plt
import matplotlib as mpl

# (a) | Prosdiorismos synarthshs metaforas kleistou brogxou

input_data_g = np.array([[1, 2], [1, 4]])           # G(s) = (s + 2) / (s + 4)
input_data_h = np.array([[1], [1, 2]])              # H(s) = 1 / (s + 2)

G = mtlb.tf(input_data_g[0][:], input_data_g[1][:])
H = mtlb.tf(input_data_h[0][:], input_data_h[1][:])
TF = mtlb.feedback(G, H)

print(TF)   # Ektpypwsh synarthshs metaforas kleistou brogxou

#_______________________________________________________________________________

# (b) | Paragwgh diagrammatos polwn - mhdenikwn

mpl.style.use('Solarize_Light2')
mtlb.pzmap(TF, Plot=True, title='Pole Zero Map')
plt.show()

#_______________________________________________________________________________

# (c) | Apaloifh koinwn polwn kai mhdenikwn sth synarthsh metaforas kleistou
#     | brogxou

TF_new = mtlb.minreal(TF)
print(TF_new)

#_______________________________________________________________________________

# (d) | Apeikonish sto idio diagramma bhmatikhs apokrish tou systhmatos gia th
#    | S.M. prin kai meta thn apaleipsh twn polwn kai twn mhdenikwn

yout1, T1 = mtlb.step(TF)
yout2, T2 = mtlb.step(TF_new)
plt.title('Step Reponse')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.plot(T1, yout1,'g',T2,yout2,'r')
plt.show()
