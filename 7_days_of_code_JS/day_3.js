/* 
* Tu desafío de hoy es crear los destinos posibles de un juego, en el que el usuario pueda elegir:

? Si quiere seguir hacia el área de Front-End o seguir hacia el área de Back-End.

? Si está en el área de Front-End, si quiere aprender React o aprender Vue. Si está en el área de Back-End, podrá aprender C# o aprender Java.

? Después, independientemente de las elecciones anteriores, el usuario podrá elegir entre seguir especializándose en el área elegida o desarrollarse para convertirse en Fullstack. Debes mostrar en pantalla un mensaje específico para cada elección.
 
? Finalmente, pregunta en qué tecnologías le gustaría a la persona especializarse o conocer. Aquí, la persona puede responder N tecnologías, una a la vez. Entonces, mientras continúe respondiendo **ok** a la pregunta: "¿Hay alguna otra tecnología que te gustaría aprender?", sigue presentando el Prompt, para que complete el nombre de la tecnología en cuestión. Y, justo después, presenta un mensaje comentando algo sobre la tecnología ingresada.
 
! Lo importante es que la persona que esté jugando siempre pueda elegir qué decisión tomar para aprender y desarrollarse en el área de programación.

* *Además, también es esencial que, al final del juego, pueda ingresar tantas tecnologías como desee en la lista de aprendizaje. 
*/

let areas = {'Front-End':['React','Vue'],'Back-End':['C#','Java']};
let selected = {};

function select (selected){
    let area = '';
    let opc;
    do {
        opc =parseInt(prompt('Que deseas aprender (elige con 1 o 2): \n 1. Front-End \n 2. Back-End'));
        console.log(typeof opc, '\n',opc)
        if (opc == 1){
            area='Front-End';
            selected[area]=[];
            return selected;
        } else if (opc == 2){
            area='Back-End';
            selected[area]=[];
            return selected;
        } else{
            alert('Dato invalido, por favor ingresa 1 o 2');    
        }
    } while(opc != 1 && opc != 2)
}

function areaEsp(userSelection){
    let framework_language=0;
    do{
        if ('Front-End' in userSelection){
            framework_language = parseInt(prompt('Que framework deseas utilizar:\n1. React \n2. Vue'));
            if (framework_language == 1){
                userSelection['Front-End'].push('React');
                return userSelection;
            } else if (framework_language == 2){
                userSelection['Front-End'].push('Vue');
                return userSelection;
            }
        }else if ('Back-End' in  userSelection){
            framework_language = parseInt(prompt('Que lenguaje deseas utilizar:\n1. C# \n2. Java'));
            if (framework_language == 1){
                userSelection['Back-End'].push('C#')
                return userSelection;
            } else if (framework_language == 2){
                userSelection['Back-End'].push('Java')
                return userSelection;
            } 
        }else{
            alert('Dato invalido, por favor ingresa 1 o 2');
        }
    }while (framework_language!=1 && framework_language!=2)
}

function ultimaEleccion(userSelection) {
    let enfoque;
    let area;
    do{
        enfoque = parseInt(prompt(`¿Quieres?: \n1. ¿Especializarte mas en ${'Front-End' in userSelection ? 'Front-End':'Back-End'}? \n2. ¿Deseas ser Fullstack?\n`));
        if (enfoque == 1){
            area = 'Front-End' in userSelection ? 'Front-End' : 'Back-End';
            return [area,userSelection]
        }else if (enfoque == 2){
            area = 'Front-End' in userSelection ? 'Back-End':'Front-End';
            userSelection[area]=[];
            return [area,userSelection] 
        }else{
            alert('Dato invalido, por favor ingresa 1 o 2');
        }
    }while(enfoque != 1 && enfoque != 2)
}

function tecAdd(seleccion,area){
    let addArea = 1
    while(addArea != 0){
        addArea = prompt('Escribe el nombre de las tecnologias que deseas profundizar: \n(Para salir ingresa 0)\n');
        addArea == 0 ? 0 : seleccion[area].push(addArea);
    }
    return seleccion;
}

let area;
let userSelection = select(selected);
userSelection = areaEsp(userSelection);
[area,userSelection] = ultimaEleccion(userSelection);
userSelection = tecAdd(userSelection,area);

let parrafo = document.getElementById('tec');
parrafo.innerHTML = JSON.stringify(userSelection,null,2);
console.log(userSelection);