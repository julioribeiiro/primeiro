function RenderToDos(){
    lista_1.innerHTML = '';

    for (toDo of toDos){
        var elemento = document.createElement("li");
        var elemento_texto = document.createTextNode(toDo);
        var excluir = document.createElement("button");
        excluir.setAttribute("onclick", "RemoveElemento(" + toDos.indexOf(toDo) + ")");

        excluir.appendChild(document.createTextNode("Excluir"));
        elemento.appendChild(elemento_texto);
        elemento.appendChild(excluir);
        lista_1.appendChild(elemento);

    }
}

function RemoveElemento(pos){
    toDos.splice(pos, 1);
    RenderToDos();
    SaveToDos();
}

//--COMECANDO PROGRAMA-------------
var lista_1 = document.querySelector("#app ul");
var botao_1 = document.querySelector("#app button");
var input_1 = document.querySelector("#app input");

var toDos = JSON.parse(localStorage.getItem("list_todos")) || [];

botao_1.onclick = function(){
    toDos.push(input_1.value);
    input_1.value = '';
    RenderToDos();
    SaveToDos();
}

function SaveToDos(){
    localStorage.setItem("list_todos", JSON.stringify(toDos));
}

RenderToDos();//RENDERIZANDO LISTA INICIALMENTE

//COMECNADO OUTA COISA

var input_2 = document.querySelector("#segundo input");
var botao_2 = document.querySelector("#segundo button");
var lista_2 = document.querySelector("#segundo ul");
var link = '';

botao_2.onclick = function(){
    link = "https://api.github.com/users/" + input_2.value + "/repos";

    ajax.open('GET', link);
    ajax.send(null);
    lista_2.innerHTML = '';

    ajax.onreadystatechange = function() {
        if(ajax.readyState === 4){
            var repositorios = JSON.parse(ajax.responseText);
            console.log(repositorios[0]["name"]);

            
            for(repo of repositorios){
                console.log(repo["name"]);
                var novo = document.createElement("li");
                novo.appendChild(document.createTextNode(repo["name"]));
                lista_2.appendChild(novo);
            }

        }
    }

}

var ajax = new XMLHttpRequest();

