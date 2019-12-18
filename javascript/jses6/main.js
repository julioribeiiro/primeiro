function imprime(){
    setTimeout(() => {console.log("printou")}, 2000);
}

async function nada() {
    await imprime();
    await imprime();
    
}
//nada();

imprime();