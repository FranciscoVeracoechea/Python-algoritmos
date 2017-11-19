import matplotlib.pyplot as plt
import sys

error = True #boleam true /false

    
def pendiente(x1, x2, y1, y2):
  return (y2-y1)/(x2-x1)

def interseccion(x1,x2,y1,y2,x3,x4,y3,y4):
  
  if (x1 == x2):
    ma = "infinito";
  else:
    ma = pendiente(x1, x2, y1, y2)
  
  if (x3 == x4):
    mb = "infinito"
  else:
    mb = pendiente(x3, x4, y3, y4)
  
  if ma != "infinito" or mb != "infinito":
    
    if ma == mb:
      if (y1-ma*x1 == y3-mb+x3):
        resultado = "El punto de intersección es una linea, ya que las dos rectas son iguales."
        return resultado
      else:
        resultado = "Las rectas No se cruzan"
        return resultado
      
    else:
      intX = (ma * x1 - y1 - mb * x3 + y3) / (ma - mb)
      intY = mb*(intX - x3) + y3
      resultado = [intX, intY, ma, mb]
      return resultado
  
  else :
    resultado = "Error divición entre cero, no se puede calcular punto de intersección"
    
  

print("Ingrese las cooordenasdas de 2 rectas \nque sigan la formula y= mx + b")

while error:
  
  try:
    print("\nIngrese las coordenasdas de la recta 1°: ")
    x1 = int(input("Dame la coordenada de x1: ")) 
    y1 = int(input("Dame la coordenada de y1: ")) 
    x2 = int(input("Dame la coordenada de x2: "))
    y2 = int(input("Dame la coordenada de y2: "))
    
    print("\nIngrese las coordenasdas de la recta 2°: ")
    x3 = int(input("Dame la coordenada de x3: ")) 
    y3 = int(input("Dame la coordenada de y3: ")) 
    x4 = int(input("Dame la coordenada de x4: "))
    y4 = int(input("Dame la coordenada de y4: "))
    
    r = interseccion(x1,x2,y1,y2,x3,x4,y3,y4)
    
    if isinstance(r, str):
      print("\n"+r+"\n")
      plt.plot([x1, y1], [x2, y2], "b-", linewidth=2, label="L1")
      plt.plot([x3, x4], [y3, y4], "r-", linewidth=2, label="L2")
      error = False
    else:
      print("\nPunto de intersección ("+str(r[0])+", "+str(r[1])+")")
      plt.plot([x1, x2], [y1, y2], "b-", linewidth=2, label="L1")
      plt.plot([x3, x4], [y3, y4], "r-", linewidth=2, label="L2")
      plt.annotate('P.I.', xy=(r[0], r[1]), xytext=(r[0]+2, r[1]+2),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
      error = False
  
  except ValueError:
    print ("Dato no valido... ingrese solo números enteros")
    error = True


plt.grid(True)

plt.legend(loc='upper left')
plt.show()
sys.exit(0)
