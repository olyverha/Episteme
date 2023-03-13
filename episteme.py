import time
from chromedriverChatGPT import ChatGPT
from selenium.common import exceptions as seleniumexceptions
import os
import textwrap
import threading
import re
import PyPDF2
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from fpdf import FPDF


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def open_file(filepath):
    with open(filepath, 'r', encoding='UTF-8') as infile:
        return infile.read()


def save_file(content, filepath):
    with open(filepath, 'w', encoding='UTF-8') as out_file:
        out_file.write(content)


if __name__ == '__main__':
    Tk().withdraw()
    filelocation = askopenfilename()
    tituloDoc = os.path.basename(filelocation)
    tituloDoc = os.path.splitext(tituloDoc)[0]

    with open(filelocation, "rb") as f:
        pdf = PyPDF2.PdfReader(f)
        alltext = ""
        for pageNum in range(len(pdf.pages)):
            pageObj = pdf.pages[pageNum]
            alltext += pageObj.extract_text()
    # save_file(alltext, 'output_%s.txt' % time())
    # alltext = open_file('input.txt')
    alltext = re.sub('\\s+', ' ', alltext)
    chunks = textwrap.wrap(alltext, 2000)
    result = list()
    result_analise = list()
    while True:
        token = open_file('token.txt')
        session_token = token.replace('\n', '')
        conversation_id = ''
        chat = ChatGPT(session_token, conversation_id)
        break
    clear_screen()
    print(
        'Iniciando o resumo do documento...\n'
    )

    def algoritimo_summary(cont):
        contador_geral = cont
        event = threading.Event()
        contador_interno = 0

        def consulta(_prompt):
            resultado = chat.send_message(_prompt)
            event.set()  # envia o sinal para o event.wait() continuar
            return resultado

        for chunk in chunks:
            if contador_geral > contador_interno:
                contador_interno += 1
            else:
                prompt = open_file('prompt.txt').replace('<<SUMMARY>>', chunk)
                prompt = prompt.encode(encoding='UTF-8', errors='ignore').decode('UTF-8')
                summary = consulta(prompt)
                event.wait()  # aguarda o sinal para continuar
                event.clear()  # limpa o sinal para a próxima iteração
                text = summary['message'].strip()  # pega somente o conteúdo da mensagem sem o conversation_id
                text = re.sub('\\s+', ' ', text)  # substitui todas as ocorrências de um ou mais espaços em branco por
                #                                   um único espaço em branco
            #   filename = '%s_gpt3.txt' % time()
            #   with open('gpt3_logs/%s' % filename, 'w') as outfile:
            #       outfile.write('PROMPT:\n\n' + prompt + '\n\n==========\n\nRESPONSE:\n\n' + text)
                print('\n\n\n', contador_geral + 1, 'of', len(chunks), ' - ', text)
                result.append(text)
                contador_geral += 1
                contador_interno += 1

    #  Cria a análise baseada no resumo
    def algoritimo_analisis(summary, questions):
        event = threading.Event()
        count = 0
        resumo = summary
        resumo = re.sub('\\s+', ' ', resumo)
        perguntas = questions
        sentences = perguntas.split('<<NEW QUESTION>>')

        def consulta_analise(_prompt):
            resultado = chat.send_message(_prompt)
            event.set()  # envia o sinal para o event.wait() continuar
            return resultado

        for sentence in sentences:
            prompt = open_file('prompt_analise.txt').replace('<<QUESTION>>', sentence)
            prompt = prompt.replace('<<SUMMARY>>', resumo)
            prompt = prompt.encode(encoding='UTF-8', errors='ignore').decode('UTF-8')
            summary = consulta_analise(prompt)
            event.wait()  # aguarda o sinal para continuar
            event.clear()  # limpa o sinal para a próxima iteração
            text = summary['message'].strip()  # pega somente o conteúdo da mensagem sem o conversation_id
            text = re.sub('\\s+', ' ', text)  # substitui todas as ocorrências de um ou mais espaços em branco por
            #                                   um único espaço em branco
            #   filename = '%s_gpt3.txt' % time()
            #   with open('gpt3_logs/%s' % filename, 'w') as outfile:
            #       outfile.write('PROMPT:\n\n' + prompt + '\n\n==========\n\nRESPONSE:\n\n' + text)
            print('\n\n\n', count + 1, 'of', len(sentences), ' - ', text)
            result_analise.append(sentence + ':' + '\n' + text)
            count += 1


    #  Executa o programa
    try:
        algoritimo_summary(0)
        tempo_atual = time.time()
        data_hora_formatada = time.strftime('%d%m%Y_%H%M%S', time.localtime(tempo_atual))

        # data_hora_formatada = '13032023_002247'  # apagar

        titulo_resumo = tituloDoc + '_RESUMO_' + '[' + data_hora_formatada + ']' + '.txt'
        save_file('\n\n'.join(result), 'repositorio/' + titulo_resumo)
        time.sleep(2)  # aguarda salvar o arquivo em disco
        print(
            'Iniciando a análise do documento...\n'
        )
        algoritimo_analisis(open_file('repositorio/' + titulo_resumo), open_file('questions.txt'))
        titulo_analise = tituloDoc + '_ANALISE_' + '[' + data_hora_formatada + ']' + '.txt'
        save_file('\n\n'.join(result_analise), 'repositorio/' + titulo_analise)

        with open('repositorio/' + titulo_resumo, 'r', encoding='utf-8') as f1, open(
                'repositorio/' + titulo_analise, 'r', encoding='utf-8') as f2:
            conteudo_arquivo1 = f1.read()
            conteudo_arquivo2 = f2.read()

        with open('repositorio/' + tituloDoc + '_RESUMO_ANALISE_' + '.txt', 'w') as f3:
            f3.write('RESUMO_' + tituloDoc + '[' + data_hora_formatada + ']' + '\n' + conteudo_arquivo1 + '\n\n\n')
            f3.write('ANALISE_' + tituloDoc + '[' + data_hora_formatada + ']' + '\n' + conteudo_arquivo2)

        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_title('RESUMO E ANÁLISE DE ' + tituloDoc)

        pdf.set_font('Arial', '', 12)

        with open('repositorio/' + titulo_resumo, 'r', encoding='utf-8') as f:
            text = f.read()
            pdf.cell(0, 10, text, ln=True)

        with open('repositorio/' + titulo_analise, 'r', encoding='utf-8') as f:
            text = f.read()
            pdf.cell(0, 10, text)

        nomePDF = 'repositorio/RESUMO_ANALISE_' + tituloDoc + '.pdf'
        pdf.output(nomePDF)
        """

    except seleniumexceptions.TimeoutException:
        print('.Limite de tempo de espera da requisição atingido. Execute novamente o programa.')
    except ValueError as v:
        if 'Too many requests in 1 hour' in v:
            print('Limite de consultas em uma hora atingida. Aguarde ou informe o session-token de uma conta '
                  'diferente.')
        elif 'Incorrect API key provided' in v:
            print('Incorrect API key provided: undefined. Erro de comunicação, tente novamente.')
        else:
            print(v)
