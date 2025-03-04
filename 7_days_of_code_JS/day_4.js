/* 
? Debes crear un pequeño programa que comience con un valor específico predefinido entre 0 y 10 para el número que vas a adivinar (por ejemplo, el 7).

* A continuación, el programa te preguntará cuál es el valor que deseas adivinar y, si aciertas, te felicitará. Si te equivocas, te dará 2 intentos más.

* Al final, si no aciertas en ninguno de los intentos, imprimirá cuál era el número inicial.

* Después de que el programa esté funcionando, intenta usar un número aleatorio en lugar de uno predefinido. 
*/

let numSecret = Math.floor(Math.random()*11);
let intento = "";

function intentos(){
    for (let i = 0 ; i<3;i++){
        intento = prompt('Intenta admivinar el numero entre 0 y 10');
        if (numSecret==intento){
            alert(`Felicidades, acertaste! El número era ${numSecret}.`);
            return true;
        }else{
        alert(`Incorrecto te quedan ${2-i} intentos`);
        }
    }
    return false;
}

intentos() == false && alert(`Lo siento, no acertaste, el numero era ${numSecret}`);

