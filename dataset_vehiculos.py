import pandas as pd
import random
import os 

os.system("clear")

random.seed(42)

n = 100
marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes', 'Audi', 'Volkswagen', 'Hyundai']
modelos = ['Sedán', 'SUV', 'Camioneta', 'Hatchback', 'Coupe', 'Convertible', 'Minivan', 'Pickup']
tipos_combustible = ['Gasolina', 'Diésel', 'Híbrido', 'Eléctrico', 'Gas']
transmisiones = ['Manual', 'Automática', 'CVT', 'Semi-automática']

df = pd.DataFrame({
    'id_vehiculo': range(1, n+1),
    'marca': [random.choice(marcas) for _ in range(n)],
    'modelo': [random.choice(modelos) for _ in range(n)],
    'año': [random.randint(2015, 2024) for _ in range(n)],
    'kilometraje': [random.randint(0, 150000) for _ in range(n)],
    'precio': [random.randint(150000, 800000) for _ in range(n)],
    'tipo_combustible': [random.choice(tipos_combustible) for _ in range(n)],
    'transmision': [random.choice(transmisiones) for _ in range(n)],
    'num_puertas': [random.choice([2, 3, 4, 5]) for _ in range(n)],
    'potencia': [random.randint(80, 400) for _ in range(n)],
    'consumo_ciudad': [round(random.uniform(8.0, 25.0), 1) for _ in range(n)],
    'consumo_carretera': [round(random.uniform(6.0, 20.0), 1) for _ in range(n)]
})
#Eficiencia de consumo: Ciudad y Carretera

# Primer inciso
print("Primer Inciso:")
print(df)

# Segundo inciso
print("Segundo Inciso:")
dimensiones = df.shape
print(f"Dimensiones: {dimensiones}")
columnas = df.columns
print(f"Columnas: {columnas}")
tipo_datos = df.dtypes
print("Tipos de datos: {}".format(tipo_datos))

#Tercer inciso
print("Tercer Inciso:")
print(df.describe())

#Cuarto inciso
print("Cuarto Inciso:")
filtro = df[df['precio'] < 350000]
print(filtro)

#Quinto inciso
print("Quinto Inciso:")
subconjunto = df.loc[df['marca'] == 'Toyota', ['id_vehiculo', 'año', 'precio']]
print(subconjunto)

#Sexto inciso
print("Sexto Inciso:")
subconjunto_loc = df.loc[0:9, ['id_vehiculo', 'marca', 'modelo']]
print(subconjunto_loc)

#Septimo inciso


