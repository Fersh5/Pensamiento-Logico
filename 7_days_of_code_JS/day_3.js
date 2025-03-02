/* 
* Tu desafío de hoy es crear los destinos posibles de un juego, en el que el usuario pueda elegir:

? Si quiere seguir hacia el área de Front-End o seguir hacia el área de Back-End.

? Si está en el área de Front-End, si quiere aprender React o aprender Vue. Si está en el área de Back-End, podrá aprender C# o aprender Java.

? Después, independientemente de las elecciones anteriores, el usuario podrá elegir entre seguir especializándose en el área elegida o desarrollarse para convertirse en Fullstack. Debes mostrar en pantalla un mensaje específico para cada elección.
 
? Finalmente, pregunta en qué tecnologías le gustaría a la persona especializarse o conocer. Aquí, la persona puede responder N tecnologías, una a la vez. Entonces, mientras continúe respondiendo **ok** a la pregunta: "¿Hay alguna otra tecnología que te gustaría aprender?", sigue presentando el Prompt, para que complete el nombre de la tecnología en cuestión. Y, justo después, presenta un mensaje comentando algo sobre la tecnología ingresada.
 
! Lo importante es que la persona que esté jugando siempre pueda elegir qué decisión tomar para aprender y desarrollarse en el área de programación.

* *Además, también es esencial que, al final del juego, pueda ingresar tantas tecnologías como desee en la lista de aprendizaje. */

let areas ={'FrontEnd':[],'Backend':[]}
let area = prompt('Que deseas aprender (elige con "1" o "2"): \n 1. FrontEnd \n 2. BackEnd');

let enfoque = prompt(`¿Quieres especializarte mas en ${areas[area+1]} (Opcion: 1) ? \no ¿Deseas ser Fullstack? (Opcion: 2)\n`)
if (area+1 == 1){
    area['FrontEnd']+=[]
    
}

let rea = {
    s:5

}