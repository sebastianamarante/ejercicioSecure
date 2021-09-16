# ejercicioSecure

i.sebastianamarante@gmail.com - Desafio Secure

Respuestas del desafio:

Version 01

1) En la terminal ejecutar la linea: python main.py


2) Utilizando selenium web driver podemos obtener dicho atributo con el siguiente codigo:

def test_get_atributte(self):
	driver = self.driver
	get_atributte = 			driver.find_element_by_id('search_input').get_attribute("autocomplete'')
	
	

3)  hace que WebDriver espere a que se produzca una determinada condición antes de continuar con la ejecución,
 en este caso verificamos que el LINK_TEXT llamado ACCOUNT este visible para luego poder hacerle click


4) Con el codigo anterior le decimos al driver que espere en nuestro navegador implicitamente 20 segundos 
antes de realizar la siguiente acción. 
	
5) En este codigo por ejemplo seleccionando de un drop-down primero encontramos el elemento con su name con valor de 
'amount' y seleccionamos el que tenga valor de 3


6) 
Caso 1: Verificar que el script elimine caracteres especiales - Prioridad Alta
Caso 2:  Verificar que el script cuente las palabras repetidas - Prioridad Alta
Caso 3: Validar que el programa muestre cuantas palabras se ingresaron - Prioridad Alta
Caso 4: Validar que el programa muestre el top-5 de palabras - Prioridad Alta
Caso 5: Validar que el programa no muestre palabras con un solo uso - Prioridad Media 
Caso 6: Repetir muchas veces una palabra - Prioridad Baja
Caso 7: Probar ingresando numeros - Prioridad Baja
Caso 8: Verificar que el texto de las impresiones sean la de la documentación - Prioridad Media
Caso 9: Exceder limite de palabras - Prioridad Baja

		
