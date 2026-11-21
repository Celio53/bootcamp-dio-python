# -*- coding: utf-8 -*-
"""
Prática: Desafio de Código - Classificação de Média Final do Aluno
Equivalente ao desafio JavaScript da DIO, implementado e testado em Python.

Regras:
- Média < 5        -> REP (Reprovado)
- Média >= 5 e < 7 -> REC (Recuperação)
- Média >= 7       -> APR (Aprovado)
"""

def classificar_media(media: float) -> str:
    """Classifica a média do aluno com base nos critérios do desafio."""
    if media < 5:
        return "REP"
    elif 5 <= media < 7:
        return "REC"
    else:
        return "APR"


def executar_testes_automaticos():
    """Roda os casos de teste oficiais apresentados na DIO."""
    print("=" * 50)
    print("🧪 EXECUTANDO OS TESTES OFICIAIS DO DESAFIO (DIO)")
    print("=" * 50)
    
    casos_de_teste = [
        {"entrada": 5.5, "esperado": "REC"},
        {"entrada": 8.0, "esperado": "APR"},
        {"entrada": 2.0, "esperado": "REP"},
    ]
    
    for i, caso in enumerate(casos_de_teste, start=1):
        resultado = classificar_media(caso["entrada"])
        status = "✅ PASSOU" if resultado == caso["esperado"] else "❌ FALHOU"
        print(f"Caso {i}: Média {caso['entrada']} -> Saída: {resultado} (Esperado: {caso['esperado']}) | {status}")
    
    print("=" * 50)


if __name__ == "__main__":
    # 1. Executa os testes automatizados
    executar_testes_automaticos()
    
    # 2. Permite testar interativamente se desejar
    print("\n💡 Teste você mesmo:")
    try:
        nota = float(input("Digite uma média para testar (ex: 6.2): "))
        resultado = classificar_media(nota)
        print(f"Resultado final: {resultado}")
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")
