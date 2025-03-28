/* 
* Crear un programa que pregunte si deseas agregar un alimento a tu lista de compras, y debes poder responder con "sí" o "no".

* A continuación, preguntará qué alimento deseas agregar, y escribirás su nombre, como por ejemplo "zanahoria".

* Después, deberá preguntar en qué categoría se encaja ese alimento, con algunas opciones ya predefinidas, como frutas, lácteos, congelados, dulces y lo que más creas interesante. Así podrás separar todo en su respectivo grupo.

* Por último, en caso de que ya no quieras agregar nada más a la lista de compras y respondas "no" a la primera pregunta, se mostrará una lista con todos los ítems agrupados, de la siguiente manera:

? banana, leche en polvo, tomate, leche vegetal, chicle, gominola, manzana, uva, aguacate y leche de vaca.

* El programa debería imprimir, por ejemplo:

TODO Lista de compras:
* Frutas: banana, tomate, manzana, uva, aguacate
* Lácteos: leche vegetal, leche de vaca, leche en polvo
* Congelados: 
* Dulces: chicle y gominola 
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

opc = showOpc(categorias); 
let parrafo = document.getElementById('list');
parrafo.innerHTML = opc;
