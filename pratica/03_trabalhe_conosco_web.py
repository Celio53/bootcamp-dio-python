import csv
import os
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

# ==============================================================================
# PROJETO 03: Portal Web "Trabalhe Conosco" - Captação de Motoristas & Manobristas
# ==============================================================================

DIRETORIO_SCRIPT = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_PLANILHA = os.path.join(DIRETORIO_SCRIPT, "candidatos_motoristas.csv")

def salvar_na_planilha(candidato):
    """Garante cabeçalho e adiciona a linha com o candidato.
    Se o Excel estiver aberto e travar o arquivo, salva em um arquivo de backup para não perder o dado!
    """
    arquivo_alvo = ARQUIVO_PLANILHA
    try:
        existe = os.path.exists(arquivo_alvo)
        with open(arquivo_alvo, mode="a", newline="", encoding="utf-8-sig") as f:
            escritor = csv.writer(f, delimiter=";")
            if not existe:
                escritor.writerow([
                    "Data Cadastro", "Nome", "Telefone", "CNH", "EAR",
                    "Toxicologico", "Curso Coletivo Valido", "Experiencia (anos)",
                    "Pontuacao (0-100)", "Vaga Recomendada", "Status Triagem"
                ])
            escritor.writerow([
                candidato["data_hora"],
                candidato["nome"],
                candidato["telefone"],
                candidato["cnh"],
                candidato["ear"],
                candidato["toxicologico"],
                candidato["curso_coletivo"],
                candidato["anos_exp"],
                candidato["pontos"],
                candidato["vaga_recomendada"],
                candidato["status"]
            ])
    except PermissionError:
        # Se o Excel estiver bloqueando o arquivo principal, salvamos num arquivo alternativo temporário
        arquivo_backup = os.path.join(DIRETORIO_SCRIPT, "candidatos_fila_pendente.csv")
        existe_bkp = os.path.exists(arquivo_backup)
        with open(arquivo_backup, mode="a", newline="", encoding="utf-8-sig") as f:
            escritor = csv.writer(f, delimiter=";")
            if not existe_bkp:
                escritor.writerow([
                    "Data Cadastro", "Nome", "Telefone", "CNH", "EAR",
                    "Toxicologico", "Curso Coletivo Valido", "Experiencia (anos)",
                    "Pontuacao (0-100)", "Vaga Recomendada", "Status Triagem"
                ])
            escritor.writerow([
                candidato["data_hora"],
                candidato["nome"],
                candidato["telefone"],
                candidato["cnh"],
                candidato["ear"],
                candidato["toxicologico"],
                candidato["curso_coletivo"],
                candidato["anos_exp"],
                candidato["pontos"],
                candidato["vaga_recomendada"],
                candidato["status"]
            ])
        print(f"⚠️ Atenção: A planilha principal estava aberta no Excel! Os dados foram salvos com segurança em '{arquivo_backup}'.")

def avaliar_candidato(nome, telefone, cnh, ear, toxicologico, curso_coletivo, anos_exp):
    motivo_descarte = ""
    if cnh not in ["D", "E"]:
        motivo_descarte = "CNH incompatível (Necessário CNH D ou E)"
    elif ear != "S":
        motivo_descarte = "Não possui EAR na CNH"
    elif toxicologico != "S":
        motivo_descarte = "Exame toxicológico pendente ou vencido"

    pontos = 0
    vaga_recomendada = ""
    status = ""
    mensagem_candidato = ""

    if motivo_descarte:
        pontos = 0
        vaga_recomendada = "Nenhuma no momento"
        status = f"🔴 REPROVADO ({motivo_descarte})"
        mensagem_candidato = f"""
            Olá, <strong>{nome}</strong>! Agradecemos sinceramente seu interesse em fazer parte da nossa empresa.<br><br>
            Neste momento, nossas oportunidades exigem habilitação profissional categoria D ou E com EAR e Toxicológico em dia.<br><br>
            Guardaremos seu registro em nosso banco de talentos para futuras oportunidades.
        """
    else:
        # Se os documentos básicos estão em dia:
        if anos_exp == 0:
            pontos = 65
            if curso_coletivo == "S":
                pontos += 10
            vaga_recomendada = "Manobrista de Garagem / Pátio"
            status = "🔵 APROVADO P/ MANOBRISTA (Oportunidade Inicial)"
            mensagem_candidato = f"""
                Olá, <strong>{nome}</strong>! 🎉<br><br>
                Temos uma ótima notícia: seu perfil foi pré-selecionado para a vaga de <strong>Manobrista de Garagem / Pátio</strong>!<br><br>
                Sabemos da sua vontade de ingressar na área e valorizamos quem quer começar conosco.<br><br>
                <strong>Nosso time de Recursos Humanos entrará em contato pelo WhatsApp ({telefone})</strong> nos próximos dias para agendar sua entrevista e teste de pátio.
            """
        else:
            pontos = 50 if anos_exp >= 5 else (35 if anos_exp >= 2 else 20)
            pontos += 20 if cnh == "E" else 15

            if curso_coletivo == "S":
                pontos += 30
                vaga_recomendada = "Motorista de Transporte Coletivo"
                status = "🟢 APROVADO: MOTORISTA DE TRANSPORTE COLETIVO" if pontos >= 80 else "🟡 BANCO DE RESERVA: TRANSPORTE COLETIVO"
                mensagem_candidato = f"""
                    Olá, <strong>{nome}</strong>! Parabéns! 🚍👏<br><br>
                    Seu perfil foi <strong>aprovado na triagem inicial</strong> para a posição de <strong>Motorista de Transporte Coletivo</strong>!<br><br>
                    Sua experiência comprovada e a habilitação com curso de passageiros em dia atendem perfeitamente aos nossos requisitos operacionais.<br><br>
                    <strong>O setor de RH entrará em contato pelo telefone/WhatsApp ({telefone})</strong> para dar início ao processo seletivo e agendar o teste prático!
                """
            else:
                pontos += 5
                vaga_recomendada = "Manobrista / Apoio de Cargas (Pendente Curso Passageiros)"
                status = "🟠 INDICADO P/ MANOBRISTA (Falta Curso Coletivo)"
                mensagem_candidato = f"""
                    Olá, <strong>{nome}</strong>! Agradecemos sua inscrição.<br><br>
                    Identificamos sua experiência ao volante, porém para conduzir veículos com passageiros a legislação exige o Curso de Transporte Coletivo.<br><br>
                    Seu perfil foi direcionado para oportunidades de <strong>Manobrista / Apoio Operacional</strong>.<br><br>
                    <strong>Nosso RH entrará em contato pelo WhatsApp ({telefone})</strong> para apresentar as opções disponíveis!
                """

    return {
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "nome": nome,
        "telefone": telefone,
        "cnh": cnh,
        "ear": ear,
        "toxicologico": toxicologico,
        "curso_coletivo": curso_coletivo,
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
            try:
                anos_exp = int(dados.get("anos_exp", [0])[0])
            except ValueError:
                anos_exp = 0

            # 1. Avalia candidato com as regras de RH
            candidato = avaliar_candidato(nome, telefone, cnh, ear, toxicologico, curso_coletivo, anos_exp)

            # 2. Salva na planilha CSV
            salvar_na_planilha(candidato)

            # 3. Monta a resposta HTML substituindo as tags com segurança
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
    print("=" * 70)
    print(f" 🌐 PORTAL TRABALHE CONOSCO NO AR!")
    print(f" 👉 Abra no navegador: http://localhost:{porta}")
    print("=" * 70)
    print("Pressione CTRL + C no terminal quando desejar parar o servidor.")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor finalizado com sucesso.")

if __name__ == "__main__":
    iniciar_servidor(porta=5000)
