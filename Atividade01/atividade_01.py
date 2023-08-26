import matplotlib.pyplot as plt
import math 

lista_tempo = []
lista_posicao_x = []
lista_posicao_y = []
tempo = 0.0
dt = 0.1
y_0 = 0.00
v_0 = 18.00
g = 9.8
angulo = 80 

while tempo<3.7:
    v_0y = v_0*math.sin(math.radians(angulo))
    v_t = v_0 + v_0y * tempo - 0.5 * g * tempo**2
    x_t = v_0*math.cos(math.radians(angulo))*tempo
    tempo = tempo + dt
    lista_posicao_x.append(x_t)
    lista_posicao_y.append(v_t)
print(lista_posicao_x)
print(lista_posicao_y)
plt.xlabel('$x$($m$)')
plt.ylabel('$y$(m)')
plt.plot(lista_posicao_x,lista_posicao_y)
plt.show()
plt.title('Trajetória do projétil')