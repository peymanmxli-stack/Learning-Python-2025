# 🐾 Sistema de Veterinaria "Patitas Felices"

Proyecto de práctica de **Programación Orientada a Objetos (POO) en Python**.
Este sistema simula la gestión básica de una veterinaria, permitiendo registrar animales, gestionar consultas médicas y aplicar servicios específicos según el tipo de animal.

---

## 🎯 Objetivo

Aplicar los **principios fundamentales de la Programación Orientada a Objetos**:

* Encapsulamiento
* Herencia
* Polimorfismo
* Uso de getters y métodos de clase

---

## 📁 Estructura del Proyecto

```
veterinaria_poo/
│
├── animal.py      # Clase base Animal
├── perro.py       # Clase Perro (hereda de Animal)
├── gato.py        # Clase Gato (hereda de Animal)
├── ave.py         # Clase Ave (hereda de Animal)
├── main.py        # Programa principal
└── README.md
```

---

## 🐶 Clases del Sistema

### Animal (Clase Base)

Contiene atributos y métodos comunes para todos los animales:

**Atributos**

* nombre
* edad
* peso
* dueño
* código
* vacunado
* historial de consultas

**Métodos**

* `vacunar()`
* `agregar_consulta()`
* `cambiar_peso()`
* `contar_consultas()`
* `hacer_sonido()`
* `mostrar_info()`

---

### Perro

Hereda de `Animal` y añade:

**Atributos**

* raza
* adiestrado

**Métodos**

* `adiestrar()`
* `pasear()`

---

### Gato

Hereda de `Animal` y añade:

**Atributos**

* color
* vive en interior

**Métodos**

* `cambiar_ambiente()`
* `cortar_uñas()`

---

### Ave

Hereda de `Animal` y añade:

**Atributos**

* especie
* puede volar
* tamaño de jaula

**Métodos**

* `cortar_plumas()`
* `entrenar_habla()`

---

## ⚙️ Cómo ejecutar el programa

1. Abrir la terminal en la carpeta del proyecto.

2. Ejecutar:

```
python main.py
```

o

```
py main.py
```

---

## 📊 Funcionalidades del sistema

El programa permite:

* Registrar animales
* Mostrar información de todos los pacientes
* Ejecutar sonidos de cada animal (polimorfismo)
* Vacunar animales
* Registrar consultas médicas
* Ejecutar servicios especiales según el tipo de animal
* Generar un reporte final

---

## 💻 Tecnologías utilizadas

* Python 3
* Programación Orientada a Objetos (POO)

---

## 👨‍💻 Autor
PEYMAN MIYANDASHTI 
Proyecto desarrollado como práctica académica de **POO en Python**.
