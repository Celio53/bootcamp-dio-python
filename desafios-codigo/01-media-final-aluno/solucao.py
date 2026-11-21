# -*- coding: utf-8 -*-
"""
Desafio de Código DIO: Média Final do Aluno
Linguagem: Python 3
"""

def classificar_media(media: float) -> str:
    """Classifica a média do aluno em REP, REC ou APR."""
    if media < 5:
        return "REP"
    elif media >= 5 and media < 7:
        return "REC"
    else:
        return "APR"


def testar_casos_oficiais():
    """Valida os 3 exemplos oficiais do desafio."""
    testes = [
        (5.5, "REC"),
        (8.0, "APR"),
        (2.0, "REP"),
    ]
    
    print("=" * 45)
    print("Testes Automatizados do Desafio:")
    print("=" * 45)
    for nota, esperado in testes:
        obtido = classificar_media(nota)
        status = "OK" if obtido == esperado else "FALHA"
        print(f"Média: {nota:<4} | Obtido: {obtido} | Esperado: {esperado} [{status}]")
    print("=" * 45)


if __name__ == "__main__":
    testar_casos_oficiais()
    
    print("\nTeste manual:")
    try:
        entrada = float(input("Digite a média do aluno: "))
        print(f"Resultado: {classificar_media(entrada)}")
    except ValueError:
        print("Erro: digite um número válido.")
