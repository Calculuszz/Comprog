import math 

def mosteller(w, h):
    return math.sqrt(w * h) / 60

def du_bois(w, h):
    return 0.007184*(w**0.425)*(h**0.725)

def fujimoto(w, h):
    return 0.008883*(w**0.444)*(h**0.663)

def main():
    w = float(input())
    h = float(input())
    mos = mosteller(w, h)
    du = du_bois(w, h)
    fuji = fujimoto(w, h)
    print("Mosteller =",round(mos,5))
    print("Du Bois =",round(du,5))
    print("Fujimoto =",round(fuji,5))

exec(input())
