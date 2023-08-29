# El empleado llamado Juan cobró 300 dólares por mes desde enero a junio, 500 dólares de julio a octubre, y 700 dólares por mes en noviembre y en diciembre. 

# En base al escenario propuesto, se le solicita a los estudiantes que creen un pequeño programa que calcule el sueldo promedio del empleado Juan. Además, se debe indicar sí Juan se encuentra cobrando un sueldo bajo, normal o mejor de lo normal, considerando las siguientes pautas:

# a. Sueldo bajo: por debajo de 300 dólares.
# b. Sueldo normal:  entre 300 a 900.
# c. Sueldo mejor de lo normal: más de 900 dólares.

# Tip: se debe utilizar estructuras condicionales.

sueldoJuan = {'enero': 300, 'febrero': 300, 'marzo': 300, 'abril': 300, 'mayo': 300, 'junio': 300, 'julio': 500, 'agosto': 500, 'septiembre': 500, 'octubre': 500, 'noviembre': 700, 'diciembre': 700}

for key,value in sueldoJuan.items():
  print(f'Sueldo {key}: {value} dólares')

print(f'{len(sueldoJuan)} meses') #checheando que se estén utilizando los datos de los 12 meses.

sueldoTotal = 0 # inicializando la variable suledoTotal en 0.

# calculando el sueldo promedio:
for value in sueldoJuan.values(): 
  sueldoTotal = sueldoTotal + value
print(f'Total = {sueldoTotal} dólares')
sueldo_promedio = sueldoTotal / len(sueldoJuan)
print(f'Sueldo promedio = {sueldo_promedio} dólares') 

# Determinando si el sueldo promedio del empleado es bajo, normal o mejor de lo normal:
if sueldo_promedio < 300 :
  print(f'{sueldo_promedio} dólares mensuales es un sueldo bajo.')
elif sueldo_promedio > 900 :
  print(f'{sueldo_promedio} dólares mensuales es un sueldo mejor de lo normal.')
else: 
  print(f'{sueldo_promedio} dólares mensuales es un sueldo normal.')