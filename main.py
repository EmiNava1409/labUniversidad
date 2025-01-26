from clases.universidad import Universidad
from clases.profesor import Profesor
from clases.curso import Curso
from clases.estudiante import Estudiante

# Crear la universidad
universidad = Universidad("Universidad de El Salvador")

# Crear profesores
profesor1 = Profesor("Juan Perez", 30, "Masculino", "P001", "Matemáticas")
profesor2 = Profesor("Maria Lopez", 35, "Femenino", "P002", "Física")
profesor3 = Profesor("Pedro Ramirez", 40, "Masculino", "P003", "Química")

# Crear cursos y asignarlos a profesores
curso1 = Curso("Matemáticas", "MAT101", profesor1)
curso2 = Curso("Física", "FIS101", profesor2)
curso3 = Curso("Química", "QUI101", profesor3)

# Agregar cursos a la universidad
universidad.agregar_curso(curso1)
universidad.agregar_curso(curso2)
universidad.agregar_curso(curso3)

# Crear un estudiante
estudiante = Estudiante("Carlos Perez", 20, "Masculino", "202010101", "Ingeniería en Sistemas Informáticos")

# Imprimir detalles
print(universidad)
print("\nDetalles del Estudiante:")
print(estudiante)
print("--------------------------------------------------")

print("\nDetalles de un Profesor:")
print(profesor1)
print("--------------------------------------------------")

print("\nDetalles de un Curso:")
print(curso1)
print("--------------------------------------------------")

# Agregar un nuevo curso de Física
curso_nuevo = Curso("Física", "FIS102", profesor2)
universidad.agregar_curso(curso_nuevo)

print("\nUniversidad después de agregar un nuevo curso:")
print(universidad)
print("--------------------------------------------------")