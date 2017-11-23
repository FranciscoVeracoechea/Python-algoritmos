#http://www.solveet.com/exercises/Circunferencias/181/solution-1286
#https://trinket.io/python3/3a287946dd
from math import sqrt
import numpy
import matplotlib.pyplot as plt
import sys
error = True

def resta(x1,y1,x2,y2):
  return [x1 - x2 , y1 - y2]
    
def suma(x1,y1,x2,y2):
  return [x1 + x2, y1 + y2]
        
def escala(x,y,s):
  return [x*s, y*s]


print("Ingrese las cooordenasdas de 2 circunferencias")

while error:
  
  try:
    print("\nIngrese las coordenasdas de la circunferencia Nro 1: ")
    a1 = float(input("Dame la coordenada de x1: ")) 
    b1 = float(input("Dame la coordenada de y1: ")) 
    r1 = float(input("Dame la coordenada de radio Nro 1: "))
    
    print("\nIngrese las coordenasdas de la circunferencia Nro 2: ")
    a2 = float(input("Dame la coordenada de x2: ")) 
    b2 = float(input("Dame la coordenada de y2: ")) 
    r2 = float(input("Dame la coordenada de radio Nro 2: "))
    
    if [a1,b1,r1] == [a2,b2,r2]: 
      print ("\nLas circunferencias son iguales")
      
    else:
      
      if a2-a1 != 0 or b2-b1 != 0:
        #Calculamos la distancia entre centros. 
        DISTANCIA = sqrt((a2 - a1)**2 + (b2-b1)**2)
        
        #La condición para que sea secante. 
        if (r1 + r2 >= DISTANCIA): 
          # Tras igualar ambas ecuaciones, queda una recta con término 
          # independiente A y, una vez despejada una incógnita (x) y sustituyendo,
          A = (r1*r1 - r2*r2 + DISTANCIA*DISTANCIA)/(2*DISTANCIA)
          h = sqrt(r1*r1 - A*A);
          
          puntoR = []
          
          punto = resta(a1,b1,a2,b2)
          punto2 = escala(punto[0], punto[1], -A/DISTANCIA)
          puntoR = suma(punto2[0], punto2[1], a1, b1)
          
          x3 = puntoR[0] + h*(b2 - b1)/DISTANCIA
          y3 = puntoR[1] - h*(a2 - a1)/DISTANCIA
          x4 = puntoR[0] - h*(b2 - b1)/DISTANCIA
          y4 = puntoR[1] + h*(a2 - a1)/DISTANCIA
       
          if [x3,y3] == [x4,y4]:
            print("Solo se tocan en un puto ("+ str(x3) +", "+str(y3)+")")
            circle1 = plt.Circle([a1, b1], r1, color='green', linewidth=2, label="C1", fill=False)
            circle2 = plt.Circle([a2, b2], r2, color='blue', linewidth=2, label="C2", fill=False)
            ax = plt.gca()
         
          else:
            print("Puntos de corte ("+str(x3)+", "+str(y3)+") y ("+str(x4)+", "+str(y4)+")")
            circle1 = plt.Circle([a1, b1], r1, color='green', linewidth=2, label="C1", fill=False)
            circle2 = plt.Circle([a2, b2], r2, color='blue', linewidth=2, label="C2", fill=False)
            ax = plt.gca()
            ax.plot([x3, x4], [y3, y4], "r-", linewidth=2, label="P.I.")
  
            ax.legend(loc='upper left')
            error = False
          
        else:
          print("Las circunferencias no se cruzan")
          circle1 = plt.Circle([a1, b1], r1, color='green', linewidth=2, label="C1", fill=False)
          circle2 = plt.Circle([a2, b2], r2, color='blue', linewidth=2, label="C2", fill=False)
          ax = plt.gca()
          error = False
      else:
        print("Error divición entre cero, no se puede calcular punto de intersección")
        
    
  except ValueError:
    print ("Dato no valido... ingrese solo números")
    error = True
    


ax.add_artist(circle1)
ax.add_artist(circle2)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

ax.set_xlim((-20, 20))
ax.set_ylim((-20, 20))

plt.grid(True)


plt.show()
sys.exit(0)
