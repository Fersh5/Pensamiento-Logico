/* 
* * Pedir al usuario responder 3 preguntas:
TODO: - ¿Cuál es tu nombre?
TODO: - ¿Cuántos años tienes?
TODO: - ¿Qué lenguaje de programación estás estudiando?
* Al final, el sistema mostrará el mensaje:
* "Hola [nombre], tienes [edad] años y ya estás aprendiendo [lenguaje]!"
! Observa que cada información entre [ ] es una de las respuestas dadas por la persona.

? Es 100% opcional.
* Vas a complementar el código para que, después de mostrar el mensaje anterior, el programa pregunte:
TODO: ¿Te gusta estudiar [lenguaje]? Responde con el número 1 para SÍ o 2 para NO.
* Y luego, dependiendo de la respuesta, debería mostrar uno de los siguientes mensajes:
* 1 > ¡Muy bien! Sigue estudiando y tendrás mucho éxito.
* 2 > Oh, qué pena... ¿Ya intentaste aprender otros lenguajes?
*/



let name = prompt('\n¿Cuál es tu nombre?\n');
let age = prompt('\n¿Cuántos años tienes?\n');
let language = prompt('\n¿Qué lenguaje de programación estás estudiando?\n');
let info = document.querySelector('#info');
info.innerHTML=`Hola ${name}, tienes ${age} años y ya estás aprendiendo ${language}`;
// console.log(`Hola ${name}, tienes ${age} años y ya estás aprendiendo ${language}`);
let like_programming = prompt(`¿Te gusta estudiar ${language}? Responde con el número 1 para SÍ o 2 para NO.`);

let like = document.querySelector('#like');

if (like_programming==1){
    like.innerHTML = '¡Muy bien! Sigue estudiando y tendrás mucho éxito.';
}else if (like_programming==2){
    like.innerHTML = 'Oh, qué pena... ¿Ya intentaste aprender otros lenguajes?';
} else {
    alert('Opcion no Valida');
}
