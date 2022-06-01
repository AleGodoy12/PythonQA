laLista = [3, 4, 10, "txt", ["lista", "de", "laLista"],5]
print(laLista)
#es una opción de array pero no se pueden modificar en otros objetos
#en el caso de hacerlo así se usaría array para global y las listas como locales

quieroSaber=laLista[3]
print(quieroSaber) 
#para imprimir el dato q se encuentra en la lista

quieroSaber= laLista[4][1]
print(quieroSaber)
#para imprimir un elemento de una lista dentro de una lista

laLista[2]="nct"
print(laLista)
#cambia el dato que está almacenado en el indice indicado en los corchetes x el dato q le pasamos

quieroSaber=laLista[1:4] #tambien se puede poner "[2:]" para que se impriman todos lo que le siguen a ese argumento, lo mismo con ":3"
print(quieroSaber)
#imprime solo una parte de la lista ej:empiza en el 1 y termina en el cuatro excluyendo el último


