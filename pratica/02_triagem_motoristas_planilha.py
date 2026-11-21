import csv
import os
from datetime import datetime

# ==============================================================================
# PROJETO 02: Triagem Inteligente para Transporte Coletivo e Manobristas
# Trilha: Python com IA (DIO) | Regras de Negócio e Planilhas Excel
# ==============================================================================

# Garante que a planilha será salva sempre na mesma pasta deste script
DIRETORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_PLANILHA = os.path.join(DIRETORIO_SCRIPT, "candidatos_motoristas.csv")

def inicializar_planilha():
    """Cria a planilha com cabeçalho se ela ainda não existir."""
    if not os.path.exists(ARQUIVO_PLANILHA):
        with open(ARQUIVO_PLANILHA, mode="w", newline="", encoding="utf-8-sig") as f:
            escritor = csv.writer(f, delimiter=";")
            escritor.writerow([
                "Data Cadastro",
                "Nome",
                "Telefone",
                "CNH",
                "EAR",
                "Toxicologico",
                "Curso Coletivo Valido",
                "Experiencia (anos)",
                "Pontuacao (0-100)",
                "Vaga Recomendada",
                "Status Triagem"
            ])

def cadastrar_motorista():
    print("=" * 70)
    print(" 🚌 SISTEMA DE TRIAGEM DE TALENTOS - TRANSPORTE COLETIVO & GARAGEM")
    print("=" * 70)

    # 1. Coleta de dados do candidato
    nome = input("Nome completo do candidato: ").strip()
    telefone = input("WhatsApp / Telefone para contato: ").strip()
    cnh = input("Categoria da CNH (ex: B, C, D, E): ").strip().upper()
    ear = input("Possui EAR (Exerce Atividade Remunerada) na CNH? (S/N): ").strip().upper()
    toxicologico = input("Exame toxicológico está em dia? (S/N): ").strip().upper()
    curso_coletivo = input("Possui curso de Transporte Coletivo válido (Res. Contran)? (S/N): ").strip().upper()
    
    try:
        anos_exp = int(input("Quantos anos de experiência comprovada na função de motorista? "))
    except ValueError:
        anos_exp = 0

    # ---------------------------------------------------------
    # 2. Regras de Negócio de RH (Critérios Eliminatórios)
    # ---------------------------------------------------------
    motivo_descarte = ""

    if cnh not in ["D", "E"]:
        motivo_descarte = "CNH incompatível (Exige CNH D ou E para ônibus/veículos pesados)"
    elif ear != "S":
        motivo_descarte = "Não possui EAR (obrigatório para atividade remunerada)"
    elif toxicologico != "S":
        motivo_descarte = "Exame toxicológico ausente ou vencido"

    # ---------------------------------------------------------
    # 3. Direcionamento Inteligente de Vaga (IA / Lógica Heurística)
    # ---------------------------------------------------------
    pontos = 0
    vaga_recomendada = ""
    status = ""

    if motivo_descarte:
        pontos = 0
        vaga_recomendada = "Nenhuma"
        status = f"🔴 REPROVADO ({motivo_descarte})"
    else:
        # Se os documentos básicos (CNH D/E, EAR, Toxicológico) estão 100%:
        
        # CASO A: Candidato SEM experiência de estrada -> Aproveitar para MANOBRISTA
        if anos_exp == 0:
            pontos = 65
            vaga_recomendada = "Manobrista de Garagem / Pátio"
            if curso_coletivo == "S":
                pontos += 10
            status = "🔵 APROVADO P/ MANOBRISTA (Sem exp. de estrada - oportunidade inicial)"

        # CASO B: Candidato COM experiência de estrada
        else:
            # Pontuação por experiência
            if anos_exp >= 5:
                pontos += 50
            elif anos_exp >= 2:
                pontos += 35
            else:
                pontos += 20

            # Categoria E ganha um bônus de peso
            pontos += 20 if cnh == "E" else 15

            # Avaliação do Curso Obrigatório de Passageiros
            if curso_coletivo == "S":
                pontos += 30  # Curso em dia fecha a qualificação máxima
                vaga_recomendada = "Motorista de Ônibus / Transporte Coletivo"
                if pontos >= 80:
                    status = "🟢 APROVADO: MOTORISTA DE TRANSPORTE COLETIVO"
                else:
                    status = "🟡 BANCO DE RESERVA: TRANSPORTE COLETIVO"
            else:
                # Tem CNH e experiência, mas não tem o curso obrigatório para levar passageiros
                pontos += 5
                vaga_recomendada = "Manobrista / Transporte de Cargas"
                status = "🟠 INDICADO P/ MANOBRISTA (Pendente curso de passageiros para conduzir na rua)"

    # ---------------------------------------------------------
    # 4. Gravação Automática na Planilha CSV / Excel
    # ---------------------------------------------------------
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    with open(ARQUIVO_PLANILHA, mode="a", newline="", encoding="utf-8-sig") as f:
        escritor = csv.writer(f, delimiter=";")
        escritor.writerow([
            data_hora,
            nome,
            telefone,
            cnh,
            ear,
            toxicologico,
            curso_coletivo,
            anos_exp,
            pontos,
            vaga_recomendada,
            status
        ])

    # ---------------------------------------------------------
    # 5. Exibição do Parecer do RH no Terminal
    # ---------------------------------------------------------
    print("\n" + "=" * 70)
    print(f"📋 PARECER TÉCNICO DE RH: {nome.upper()}")
    print("=" * 70)
    print(f"• Telefone: {telefone}")
    print(f"• CNH: {cnh} | EAR: {ear} | Toxicológico: {toxicologico} | Curso Coletivo: {curso_coletivo}")
    print(f"• Experiência: {anos_exp} ano(s)")
    print(f"• Pontuação (Score): {pontos}/100")
    print(f"• 🎯 Vaga Recomendada: {vaga_recomendada}")
    print(f"• 📌 Status da Triagem: {status}")
    print(f"💾 Registro salvo com sucesso em: {ARQUIVO_PLANILHA}")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    inicializar_planilha()
    cadastrar_motorista()
