let nome = prompt("Digite o seu nome: ");
let idade = prompt("Digite a sua idade: ");

function minhaFuncao(){
    return(`Olá usuário! O seu nome cadastrado é ${nome}, e a idade fornecida é ${idade}!`)
}

document.getElementById("resultadoD").innerHTML = minhaFuncao();