/* 
? Crea tu propia calculadora, pero con un detalle muy importante: cada operación debe ser una función diferente en tu código.

* Primero, la persona debe elegir una opción de operación impresa por el programa en la pantalla.

* Luego, debe ingresar los dos valores que desea utilizar, y el programa imprimirá el resultado de la operación en cuestión.

* Las opciones disponibles deben ser: suma, resta, multiplicación, división, y salir. En esta última, el programa debe detenerse y mostrar un mensaje "Hasta la próxima".
 */



function menu(){
    let eleccion = 0;
    let result = 0;
    let a,b;
    while (eleccion != 5){
        eleccion = prompt('¿Que operacion deseas realizar? (1 a 5)\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n 5. Salir');
        
        if(eleccion == 1){
            result=suma(...solicitarDatos());
            alert(`El resultado de la operacion es ${result}`)
        }else if(eleccion == 2){
            result=resta(...solicitarDatos());
            alert(`El resultado de la operacion es ${result}`)
        }else if(eleccion == 3){
            result=mult(...solicitarDatos());
            alert(`El resultado de la operacion es ${result}`)
        }else if(eleccion == 4){
            [a,b]=solicitarDatos();
            if (b==0){
                alert('No se pude dividir entre "0"');
            }else{
                result=division(a,b);
                alert(`El resultado de la operacion es ${result}`)
            }
        }else if(eleccion == 5){
            alert('Hata pronto !');
            break
        }else{
            alert('Dato invalido')
        }
    }
} 

function suma(a,b){
    return a+b;
}

function resta(a,b){
    return a-b;
}
function mult(a,b){
    return a*b;
}
function division(a,b){
    return a/b;
}

function solicitarDatos(){
    let num1 = parseFloat(prompt('Ingresa el primer numero:'));
    let num2 = parseFloat(prompt('Ingresa el segundo numero:'));
    return [num1,num2];
}

menu();