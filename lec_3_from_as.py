from lec_3_my_modul import earth_mass as em
from lec_3_my_modul import gravity_constant as G
from lec_3_my_modul import sigma_steff_bolc as sgm

g = 500 * G / 10**2
print(g)

x = em * G * sgm
print (x)