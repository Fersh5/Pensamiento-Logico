/* 
? Crear la opción de eliminar algún elemento de la lista, que se mostrará junto con la pregunta: “¿deseas eliminar un alimento de la lista de compras?”.

* Si la persona elige esa opción, el programa imprimirá los elementos presentes en la lista actual, y la persona deberá escribir cuál de ellos desea eliminar.

* Después de eso, el programa eliminará el elemento de la lista e imprimirá la confirmación de que el elemento realmente ya no está allí.

* Finalmente, el programa volverá al ciclo inicial de preguntas.

* Si, al intentar eliminar el elemento, este no se encuentra en la lista, deberás mostrar un mensaje advirtiendo de ello.
* Por ejemplo: “¡No fue posible encontrar el elemento en la lista!”.

* Recuerda que la opción de eliminar un elemento solo deberá estar disponible a partir del momento en que exista al menos un elemento en la lista de compras.
*/

let categorias = [
    {'Frutas':[]},
    {'Verduras':[]},
    {'Carnes':[]},
    {'Lacteos':[]},
    {'Bebidas':[]},
    {'Dulces y Botanas':[]}
];
function genOpc(categorias){
    let opc = "" ;
    for (let i = 0;i<categorias.length;i++){
        opc+=`\n${i+1}. ${Object.keys(categorias[i])}: ${Object.values(categorias[i])}`;
    }return opc;
}
function showOpc(categorias){
    let opc = "" ;
    for (let i = 0;i<categorias.length;i++){
        opc+=`\n<br>${i+1}. ${Object.keys(categorias[i])}: ${Object.values(categorias[i])}`;
    }return opc;
}

let opc = genOpc(categorias);
let question;
do{
    question = prompt('¿Deseas añadir un producto a tu lista de compras?\nResponde con si o no').toLocaleLowerCase();
    if (question == 'si') {
        addelement(opc,categorias)
    }
}while (question == 'si');

function addelement(opc,categorias){
    let element = prompt('Escribe el producto que deseas comprar: ');
    let categoria = prompt(`Escribe el numero en el corresponde a su categoria: ${opc}`);
    categorias[categoria-1][Object.keys(categorias[categoria-1])].push(element);
} 
function deleteElement(opc,categorias){
    let deleteE;
    let showProducts= '';
    let product; 
    do{
        deleteE = prompt('¿Deseas eliminar algun producto?\n(si o no)').toLocaleLowerCase();
        if (deleteE=='si'){
            selectCategorDelete = prompt(`¿Cual es el numero de la categoria?\n ${opc}`);
            if (categorias[selectCategorDelete-1][Object.keys(categorias[selectCategorDelete-1])[0]].length==0){
                alert(`No hay productos para eliminar`);
            }else{
                for (let i=0; i<categorias[selectCategorDelete-1][Object.keys(categorias[selectCategorDelete-1])[0]].length;i++){
                    showProducts += `\n${i+1}. ${categorias[selectCategorDelete-1][Object.keys(categorias[selectCategorDelete-1])[0]][i]}`;
                    console.log(showProducts);   
                }
                product = prompt(`Escribe el numero de producto que quieres eliminar: ${showProducts}`);
                categorias[selectCategorDelete-1][Object.keys(categorias[selectCategorDelete-1])].splice(product-1,1);
                alert('Se elimino correctamente')
            }
        }else if (deleteE == 'no'){
            alert('Vuelve pronto, buen dia!');
        }else{
            alert('Opcion no valida, ingres: si o no')
        }
    }while(deleteE!='no')
}

opc = showOpc(categorias); 
let parrafo = document.getElementById('list');
parrafo.innerHTML = opc;
opc =genOpc(categorias)
deleteElement(opc,categorias)
opc=showOpc(categorias)
parrafo.innerHTML = opc;
