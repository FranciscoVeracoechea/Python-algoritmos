#http://www.solveet.com/exercises/Circunferencias/181/solution-1286
#https://trinket.io/python3/3a287946dd
from math import sqrt
import matplotlib.pyplot as plt
import sys
error = True

def poly2(a,b,c): 
    if a == 0: # Si a es 0 se trata de un polinomio de 1er grado. 
        if b == 0: # Comprobamos que el luser no ha introducido un término independiente. 
            x1 = c # Si es así, pues el resultado será el propio término. 
            x2 = None 
        else: 
            c = float(c) # Convertimos una variable a flotante para evitar malos resultados si b y c son enteros. 
            x1 = (-c) / b 
            x2 = None 
    else: 
        # Comprobamos que el signo del discriminante para determinar la naturaleza de las raíces. 
        if ((b**2) - (4*a*c)) < 0: 
            x1 = complex(((-b) / (2*a)), sqrt(-((b**2) - (4*a*c))) / (2*a))  
            x2 = complex(((-b) / (2*a)), - sqrt(-((b**2) - (4*a*c))) / (2*a)) 
        else:     
            x1 = complex((-b + sqrt(((b**2) - (4*a*c)))) / (2*a))
            x2 = complex((-b - sqrt(((b**2) - (4*a*c)))) / (2*a))
    return [x1, x2] 

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
        DISTANCE = sqrt((a2 - a1)**2 + (b2-b1)**2)
        
        #La condición para que sea secante. 
        if (r1 + r2 >= DISTANCE): 
          # Tras igualar ambas ecuaciones, queda una recta con término 
          # independiente F y, una vez despejada una incógnita (x) y sustituyendo, 
          # queda: Ay²+By+C = 0 
          F = (a1)**2+(b1)**2-(r1)**2-(a2)**2-(b2)**2+(r2)**2 
          A = (2*(b2-b1)**2)/(a2-a1)-1 
          B = 2*F*(b2-b1)/(a2-a1)-2*b2
          C = a1**2+b2**2-r2**2+(F**2/(2*(a2-a1)))
          
          puntoY = poly2(A, B, C)
          puntoX = []
          
          for y in puntoY: 
              puntoX.append(complex((-F-2*y*(b2-b1))/(2*(a2-a1))))
              
          
         
          print("Puntos de corte ("+str(puntoX[0])+", "+str(puntoY[0])+") y ("+str(puntoX[1])+", "+str(puntoY[1])+")")
          
          circle1 = plt.Circle([a1, b1], r1, color='green', linewidth=2, label="C1", fill=False)
          circle2 = plt.Circle([a2, b2], r2, color='blue', linewidth=2, label="C2", fill=False)
          plt.plot(puntoX, puntoY, "r-", linewidth=2, label="P.I.")
          error = False
          
        else:
          print("Las circunferencias no se cruzan")
          circle1 = plt.Circle([a1, b1], r1, color='green', linewidth=2, label="C1", fill=False)
          circle2 = plt.Circle([a2, b2], r2, color='blue', linewidth=2, label="C2", fill=False)
          error = False
      else:
        print("Error divición entre cero, no se puede calcular punto de intersección")
        
    
  except ValueError:
    print ("Dato no valido... ingrese solo números")
    error = True
    
fig, ax = plt.subplots()

ax.add_artist(circle1)
ax.add_artist(circle2)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

ax.set_xlim((-20, 20))
ax.set_ylim((-20, 20))

plt.grid(True)
plt.legend(loc='upper left')

plt.show()
sys.exit(0)
