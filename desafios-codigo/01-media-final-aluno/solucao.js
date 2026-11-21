// Desafio de Código DIO: Média Final do Aluno
// Linguagem: JavaScript

// Funções globais providas pelo ambiente da DIO:
// gets(): lê uma linha de entrada
// print(texto): imprime o texto na saída padrão

let media = gets();

if (media < 5) {
    print('REP');
} else if (media >= 5 && media < 7) {
    print('REC');
} else {
    print('APR');
}
