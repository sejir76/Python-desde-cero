'''
Por convención en Python para crear variables se debe de escribir:
    - el nombre de la variable toda en minúscula y no puede comenzar con un número
    - solo se debe de usar A-z, 0-9, and _
    - Se difiere entre mayúsculas y minúsculas
'''

# Nombres de variables validas:
'''
firstname
lastname
age
country
first_name
capital_city
current_year_2024
num1
num2


'''

# Nombres de variables invalidas:
'''
first-name
first@name
first$name
1num
num-1
'''


# Ejemplos de variables correctas

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# La función "print" soporta argumentos:
'''
print(object(s), sep=separator, end=end, file=file, flush=flush)
Parámetros:

- object(s): Es el valor o mensaje que se va a imprimir. Puede ser un solo valor o varios valores separados 
por comas.

- sep (opcional): Es el separador que se utiliza para separar los valores que se imprimen. El valor 
predeterminado es un espacio en blanco.

- end (opcional): Es el carácter que se agrega al final de la impresión. El valor predeterminado es una nueva
línea (\n).

- file (opcional): Es el objeto de archivo en el cual se va a realizar la impresión. Si no se proporciona, 
el mensaje se imprime en la consola (stdout).

- flush (opcional): Es un valor booleano que indica si el buffer de salida debe vaciarse después de la 
impresión. El valor predeterminado es False.
'''

# Concatenación de variables en un print
print(my_int_variable, my_int_to_str_variable, my_bool_variable)

print("Hello", "how are you?", sep="---")

# Función len()
'''
La función len () nos permite conocer la longitud o tamaño de una secuencia o estructura de datos3. 
Por ejemplo, si tenemos una cadena de texto, la función len () nos devuelve el número de caracteres de la 
cadena
'''
print(len(my_string_variable))

# Variables en una sola línea
'''
En el ejemplo veremos como al usar variables en una sola línea los valores que se van asignando a estas 
variables corresponde al orden de como se van escribiendo. Aunque este método no es muy recomendable ya
que puede llevar a errores y de difícil mantenimiento.
'''
name, surname, alias, age = "Rafa", "SJ", "sejir", 40
print(name, surname, age, "Y mi alias es: ", alias)

# Inputs
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuantos años tines? ')
print(name)
print(age)

# Cambiamos su tipo
name = 40
age = "Brais"
print(name)
print(age)
