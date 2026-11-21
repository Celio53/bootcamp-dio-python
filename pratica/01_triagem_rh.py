# ==============================================================================
# PROJETO 01: Assistente de Triagem de Talentos (Simulador de IA para RH)
# Trilha: Python com IA (DIO) | Ambientação
# ==============================================================================

def analisar_candidato():
    print("=" * 60)
    print(" 🤖 BEM-VINDO AO SISTEMA INTELIGENTE DE TRIAGEM DE RH")
    print("=" * 60)
    print()

    # 1. Entrada de Dados (Simulando a leitura de um currículo)
    nome = input("Digite o nome do(a) candidato(a): ").strip()
    anos_experiencia = int(input(f"Quantos anos de experiência {nome} tem na área? "))
    
    print("\nCompetências disponíveis para seleção:")
    print(" - Python")
    print(" - Excel Avançado")
    print(" - Gestão de Pessoas")
    print(" - Inteligência Artificial")
    print(" - People Analytics")
    print()

    competencias_digitadas = input(
        "Digite as competências que o candidato possui (separadas por vírgula):\n> "
    )

    # 2. Processando as competências (transformando em lista e limpando espaços)
    lista_competencias = [c.strip().lower() for c in competencias_digitadas.split(",")]

    # 3. Regras da Vaga (Perfil desejado pelo RH)
    competencias_obrigatorias = ["python", "people analytics"]
    pontos = 0

    # Avaliando experiência (Regra de Negócio)
    if anos_experiencia >= 5:
        pontos += 40
    elif anos_experiencia >= 2:
        pontos += 25
    else:
        pontos += 10

    # Avaliando competências
    for comp in competencias_obrigatorias:
        if comp in lista_competencias:
            pontos += 30  # cada competência-chave soma 30 pontos

    # 4. Resultado e Decisão Automatizada (Simulando a IA / Heurística)
    print("\n" + "-" * 60)
    print(f"📊 RELATÓRIO DE AVALIAÇÃO: {nome.upper()}")
    print("-" * 60)
    print(f"• Experiência: {anos_experiencia} anos")
    print(f"• Competências informadas: {', '.join(lista_competencias)}")
    print(f"• Pontuação de Compatibilidade (Match Score): {pontos}/100")
    print()

    if pontos >= 80:
        status = "🟢 FORTEMENTE RECOMENDADO(A) - Avançar para entrevista com gestor!"
    elif pontos >= 50:
        status = "🟡 EM ANÁLISE - Perfil interessante, avaliar para banco de talentos."
    else:
        status = "🔴 PERFIL NÃO ADERENTE - Enviar e-mail de agradecimento e feedback."

    print(f"Decisão do Sistema: {status}")
    print("=" * 60)

if __name__ == "__main__":
    analisar_candidato()
