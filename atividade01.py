# Dados os valores de horario a baixo, decifre a logica e faca um codigo para executar
# entrada 1 3:45 - entrada 2: 14:20 - saida:6:05
hora1= int(input("digite a hora: "))
minuto1= int(input("digite o minuto: "))
hora2= int(input("digite a hora: "))
minuto2= int(input("digite o minuto: "))
somahora= hora1 + hora2
somaminuto= minuto1 + minuto2
if somaminuto >=60:
   somahora += 1
if somaminuto >=60:
   somaminuto -= 60
if hora1 >= 12:
   somahora -= 12
if hora2 >= 12:
   somahora -= 12
if somahora >= 12:
   somahora -= 12
print(f"são extamente {somahora}:{somaminuto} min ")


















