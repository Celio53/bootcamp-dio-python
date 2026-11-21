import csv
import os
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

# ==============================================================================
# PROJETO 03: Portal Web "Trabalhe Conosco" - Captação de Motoristas & Manobristas
# Regras Atualizadas: Pontuação na CNH e Disponibilidade de Escala (Madrugada/FDS)
# ==============================================================================

DIRETORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_PLANILHA = os.path.join(DIRETORIO_SCRIPT, "candidatos_motoristas.csv")

def salvar_na_planilha(candidato):
    """Salva os dados do candidato na planilha com contingência se o Excel estiver aberto."""
    arquivo_alvo = ARQUIVO_PLANILHA
    colunas = [
        "Data Cadastro", "Nome", "Telefone", "CNH", "EAR",
        "Toxicologico", "Curso Coletivo Valido", "CNH Regular (<20pts)",
        "Disponibilidade Escala", "Experiencia (anos)", "Pontuacao (0-100)",
        "Vaga Recomendada", "Status Triagem"
    ]
    linha = [
        candidato["data_hora"], candidato["nome"], candidato["telefone"],
        candidato["cnh"], candidato["ear"], candidato["toxicologico"],
        candidato["curso_coletivo"], candidato["pontos_cnh"], candidato["disp_escala"],
        candidato["anos_exp"], candidato["pontos"], candidato["vaga_recomendada"],
        candidato["status"]
    ]

    try:
        existe = os.path.exists(arquivo_alvo)
        with open(arquivo_alvo, mode="a", newline="", encoding="utf-8-sig") as f:
            escritor = csv.writer(f, delimiter=";")
            if not existe:
                escritor.writerow(colunas)
            escritor.writerow(linha)
    except PermissionError:
        arquivo_backup = os.path.join(DIRETORIO_SCRIPT, "candidatos_fila_pendente.csv")
        existe_bkp = os.path.exists(arquivo_backup)
        with open(arquivo_backup, mode="a", newline="", encoding="utf-8-sig") as f:
            escritor = csv.writer(f, delimiter=";")
            if not existe_bkp:
                escritor.writerow(colunas)
            escritor.writerow(linha)

def avaliar_candidato(nome, telefone, cnh, ear, toxicologico, curso_coletivo, pontos_cnh, disp_escala, anos_exp):
    motivo_descarte = ""
    if cnh not in ["D", "E"]:
        motivo_descarte = "CNH incompatível (Necessário CNH D ou E)"
    elif ear != "S":
        motivo_descarte = "Não possui EAR na CNH"
    elif toxicologico != "S":
        motivo_descarte = "Exame toxicológico pendente ou vencido"
    elif pontos_cnh != "S":
        motivo_descarte = "CNH irregular (excesso de pontos ou suspensão ativa no Detran)"

    pontos = 0
    vaga_recomendada = ""
    status = ""
    mensagem_candidato = ""

    if motivo_descarte:
        pontos = 0
        vaga_recomendada = "Nenhuma no momento"
        status = f"🔴 REPROVADO ({motivo_descarte})"
        mensagem_candidato = f"""
            Olá, <strong>{nome}</strong>! Agradecemos sinceramente seu interesse na empresa.<br><br>
            Neste momento, os requisitos legais e operacionais exigem CNH D ou E regularizada, EAR, exame toxicológico em dia e pontuação compatível.<br><br>
            Guardaremos seu registro em nosso banco de talentos para futuras oportunidades.
        """
    else:
        # Bônus por flexibilidade de escala
        if disp_escala == "S":
            pontos += 15

        if anos_exp == 0:
            pontos += 50
            if curso_coletivo == "S":
                pontos += 10
            vaga_recomendada = "Manobrista de Garagem / Pátio"
            status = "🔵 APROVADO P/ MANOBRISTA (Oportunidade Inicial)"
            mensagem_candidato = f"""
                Olá, <strong>{nome}</strong>! 🎉<br><br>
                Temos uma ótima notícia: seu perfil foi pré-selecionado para a vaga de <strong>Manobrista de Garagem / Pátio</strong>!<br><br>
                Sabemos da sua vontade de ingressar no setor de transporte coletivo e valorizamos quem quer começar na garagem.<br><br>
                <strong>Nosso time de RH entrará em contato pelo WhatsApp ({telefone})</strong> nos próximos dias para agendar sua entrevista e teste prático de pátio.
            """
        else:
            if anos_exp >= 5:
                pontos += 40
            elif anos_exp >= 2:
                pontos += 25
            else:
                pontos += 15
            
            pontos += 15 if cnh == "E" else 10

            if curso_coletivo == "S":
                pontos += 30
                vaga_recomendada = "Motorista de Transporte Coletivo"
                status = "🟢 APROVADO: MOTORISTA DE TRANSPORTE COLETIVO" if pontos >= 80 else "🟡 BANCO DE RESERVA: TRANSPORTE COLETIVO"
                mensagem_candidato = f"""
                    Olá, <strong>{nome}</strong>! Parabéns! 🚍👏<br><br>
                    Seu perfil foi <strong>aprovado na triagem inicial</strong> para a posição de <strong>Motorista de Transporte Coletivo</strong>!<br><br>
                    Sua pontuação na CNH regular, experiência comprovada e curso de passageiros em dia atendem perfeitamente aos requisitos da nossa frota.<br><br>
                    <strong>O setor de RH entrará em contato pelo telefone/WhatsApp ({telefone})</strong> para dar início ao processo seletivo e agendamento de teste prático!
                """
            else:
                pontos += 5
                vaga_recomendada = "Manobrista / Apoio Operacional"
                status = "🟠 INDICADO P/ MANOBRISTA (Falta Curso Coletivo)"
                mensagem_candidato = f"""
                    Olá, <strong>{nome}</strong>! Agradecemos sua inscrição.<br><br>
                    Identificamos sua experiência, porém para conduzir coletivos na rua é exigido o Curso de Transporte Coletivo (Resolução Contran).<br><br>
                    Seu perfil foi direcionado para oportunidades internas de <strong>Manobrista / Garagem</strong>.<br><br>
                    <strong>Nosso RH entrará em contato pelo WhatsApp ({telefone})</strong> para apresentar as opções!
                """

    return {
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "nome": nome,
        "telefone": telefone,
        "cnh": cnh,
        "ear": ear,
        "toxicologico": toxicologico,
        "curso_coletivo": curso_coletivo,
        "pontos_cnh": pontos_cnh,
        "disp_escala": disp_escala,
        "anos_exp": anos_exp,
        "pontos": pontos,
        "vaga_recomendada": vaga_recomendada,
        "status": status,
        "mensagem_candidato": mensagem_candidato
    }

HTML_FORMULARIO = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trabalhe Conosco | Vagas de Transporte e Garagem</title>
    <style>
        * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
        body { background: #f0f4f8; margin: 0; padding: 20px; color: #1e293b; }
        .card { max-width: 600px; margin: 20px auto; background: white; border-radius: 12px; padding: 32px; box-shadow: 0 4px 14px rgba(0,0,0,0.08); }
        .header { text-align: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; margin-bottom: 24px; }
        .header h1 { margin: 0; font-size: 24px; color: #0f172a; }
        .header p { margin: 6px 0 0; color: #64748b; font-size: 14px; }
        label { display: block; font-weight: 600; margin-top: 16px; margin-bottom: 6px; font-size: 14px; color: #334155; }
        input[type="text"], input[type="tel"], input[type="number"], select {
            width: 100%; padding: 12px; border: 1px solid #cbd5e1; border-radius: 8px; font-size: 15px; outline: none; transition: border-color 0.2s;
        }
        input:focus, select:focus { border-color: #2563eb; ring: 2px #bfdbfe; }
        .hint { font-size: 12px; color: #64748b; margin-top: 4px; }
        .badge-no-curriculo { background: #dcfce7; color: #166534; padding: 8px 12px; border-radius: 8px; font-size: 13px; font-weight: 600; margin-bottom: 16px; text-align: center; }
        button {
            width: 100%; margin-top: 26px; background: #2563eb; color: white; border: none; padding: 14px; border-radius: 8px;
            font-size: 16px; font-weight: 700; cursor: pointer; transition: background 0.2s;
        }
        button:hover { background: #1d4ed8; }
    </style>
</head>
<body>
    <div class="card">
        <div class="header">
            <h1>🚍 Portal Trabalhe Conosco</h1>
            <p>Vagas para Motorista de Ônibus e Manobrista de Pátio</p>
        </div>

        <div class="badge-no-curriculo">
            ✨ Cadastro 100% Digital: Não precisa enviar currículo em papel ou PDF!
        </div>

        <form action="/candidatar" method="POST">
            <label>Nome Completo:</label>
            <input type="text" name="nome" placeholder="Ex: Celio Costa" required>

            <label>WhatsApp / Celular com DDD:</label>
            <input type="tel" name="telefone" placeholder="Ex: (51) 99260-9669" required>

            <label>Categoria da sua CNH:</label>
            <select name="cnh" required>
                <option value="">Selecione...</option>
                <option value="D">Categoria D (Transporte de Passageiros)</option>
                <option value="E">Categoria E (Veículos Articulados / Carreta)</option>
                <option value="C">Categoria C</option>
                <option value="B">Categoria B</option>
            </select>

            <label>Possui EAR (Exerce Atividade Remunerada) na CNH?</label>
            <select name="ear" required>
                <option value="S">Sim, tenho EAR</option>
                <option value="N">Não possuo EAR</option>
            </select>

            <label>Exame Toxicológico está em dia?</label>
            <select name="toxicologico" required>
                <option value="S">Sim, regularizado</option>
                <option value="N">Não / Vencido</option>
            </select>

            <label>Possui o Curso de Transporte Coletivo de Passageiros (Resolução Contran)?</label>
            <select name="curso_coletivo" required>
                <option value="S">Sim, válido e averbado</option>
                <option value="N">Não possuo este curso</option>
            </select>

            <label>Situação da CNH (Pontuação & Histórico):</label>
            <select name="pontos_cnh" required>
                <option value="S">CNH regular (menos de 20 pontos e sem processo de suspensão)</option>
                <option value="N">CNH com excesso de pontos ou bloqueio no Detran</option>
            </select>

            <label>Disponibilidade para Escala de Revezamento (Madrugada / Finais de Semana / 6x1):</label>
            <select name="disp_escala" required>
                <option value="S">Sim, total disponibilidade de horário</option>
                <option value="N">Não possuo flexibilidade para escala noturna/fim de semana</option>
            </select>

            <label>Quantos anos de experiência como motorista?</label>
            <input type="number" name="anos_exp" value="0" min="0" max="40" required>
            <div class="hint">💡 Se você não tem experiência de estrada, sem problemas! Podemos aproveitar seu perfil para a vaga de Manobrista de Garagem.</div>

            <button type="submit">Enviar Meu Cadastro para o RH</button>
        </form>
    </div>
</body>
</html>
"""

HTML_RESPOSTA = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inscrição Recebida | RH</title>
    <style>
        * { box-sizing: border-box; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        body { background: #f0f4f8; margin: 0; padding: 20px; color: #1e293b; }
        .card { max-width: 600px; margin: 30px auto; background: white; border-radius: 12px; padding: 32px; box-shadow: 0 4px 14px rgba(0,0,0,0.08); }
        .badge { display: inline-block; padding: 6px 14px; border-radius: 20px; font-weight: 700; font-size: 13px; margin-bottom: 12px; }
        .badge-green { background: #dcfce7; color: #15803d; }
        .badge-blue { background: #dbeafe; color: #1d4ed8; }
        .badge-red { background: #fee2e2; color: #b91c1c; }
        .msg-box { background: #f8fafc; border-left: 4px solid #2563eb; padding: 18px; border-radius: 6px; line-height: 1.6; font-size: 15px; margin: 20px 0; }
        .btn-novo { display: inline-block; width: 100%; text-align: center; background: #0f172a; color: white; padding: 12px; border-radius: 8px; text-decoration: none; font-weight: 600; }
    </style>
</head>
<body>
    <div class="card">
        <span class="badge {{BADGE_CLASS}}">{{STATUS_TITULO}}</span>
        <h2 style="margin: 0 0 10px;">Inscrição Processada pelo RH!</h2>
        
        <div class="msg-box">
            {{MENSAGEM_CANDIDATO}}
        </div>

        <p style="font-size: 13px; color: #64748b; text-align: center;">
            ✅ Seus dados foram arquivados com sucesso na planilha de triagem do RH.
        </p>

        <a href="/" class="btn-novo">Fazer Nova Inscrição</a>
    </div>
</body>
</html>
"""

class ServidorTrabalheConosco(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML_FORMULARIO.encode("utf-8"))

    def do_POST(self):
        try:
            tamanho = int(self.headers.get("Content-Length", 0))
            corpo = self.rfile.read(tamanho).decode("utf-8")
            dados = urllib.parse.parse_qs(corpo)

            nome = dados.get("nome", [""])[0].strip()
            telefone = dados.get("telefone", [""])[0].strip()
            cnh = dados.get("cnh", [""])[0].strip().upper()
            ear = dados.get("ear", ["N"])[0].strip().upper()
            toxicologico = dados.get("toxicologico", ["N"])[0].strip().upper()
            curso_coletivo = dados.get("curso_coletivo", ["N"])[0].strip().upper()
            pontos_cnh = dados.get("pontos_cnh", ["S"])[0].strip().upper()
            disp_escala = dados.get("disp_escala", ["S"])[0].strip().upper()
            try:
                anos_exp = int(dados.get("anos_exp", [0])[0])
            except ValueError:
                anos_exp = 0

            candidato = avaliar_candidato(nome, telefone, cnh, ear, toxicologico, curso_coletivo, pontos_cnh, disp_escala, anos_exp)
            salvar_na_planilha(candidato)

            badge_class = "badge-green" if "🟢" in candidato["status"] else ("badge-blue" if "🔵" in candidato["status"] else "badge-red")
            html_final = (
                HTML_RESPOSTA
                .replace("{{BADGE_CLASS}}", badge_class)
                .replace("{{STATUS_TITULO}}", candidato["vaga_recomendada"])
                .replace("{{MENSAGEM_CANDIDATO}}", candidato["mensagem_candidato"])
            )

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_final.encode("utf-8"))

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"Erro no processamento: {e}".encode("utf-8"))

def iniciar_servidor(porta=5000):
    servidor = HTTPServer(("0.0.0.0", porta), ServidorTrabalheConosco)
    print("=" * 72)
    print(f" 🌐 PORTAL TRABALHE CONOSCO ATUALIZADO NO AR!")
    print(f" 👉 Abra no navegador: http://localhost:{porta}")
    print("=" * 72)
    print("Pressione CTRL + C no terminal quando desejar parar o servidor.")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor finalizado com sucesso.")

if __name__ == "__main__":
    iniciar_servidor(porta=5000)
