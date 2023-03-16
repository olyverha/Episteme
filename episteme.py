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
    alltext = re.sub('\\s+', ' ', alltext)
    chunks = textwrap.wrap(alltext, 2000)
    result = list()
    result_analise = list()
    while True:
        token = open_file('token2.txt')
        session_token = token.replace('\n', '')
        conversation_id = ''
        chat = ChatGPT(session_token, conversation_id)
        break
    clear_screen()
    print(
        'Iniciando conexão com o modelo...\n'
    )
    time.sleep(10)  # tempo necessário para corrigir o erro de session expired


    def algoritimo_summary(cont):
        print(
            'Iniciando o resumo do documento...\n'
        )
        contador_geral = cont
        event = threading.Event()
        contador_interno = 0

        def consulta(_prompt):
            resultado = chat.send_message(_prompt)
            event.set()  # envia o sinal para o event.wait() continuar
            return resultado

        for chunk in chunks:
            if contador_geral > contador_interno:
                print('Salto do contador...')
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
    def algoritimo_analisis(summary, questions, char):
        print(
            'Iniciando a análise do documento...\n'
        )
        event = threading.Event()
        count = 0
        resumo = summary
        resumo = re.sub('\\s+', ' ', resumo)
        pedacos = resumo
        if char > 0:  # caso o resumo seja muito grande, precisa ser informado a quantidade de caracteres por analise
            pedacos = textwrap.wrap(resumo, char)
        perguntas = re.sub('\\s+', ' ', questions)
        sentences = perguntas.split('<<NEW QUESTION>>')

        def consulta_analise(_prompt):
            resultado = chat.send_message(_prompt)
            event.set()  # envia o sinal para o event.wait() continuar
            return resultado

        if char > 0:
            cont = 1
            for pedaco in pedacos:
                for sentence in sentences:
                    prompt = open_file('prompt_analise.txt').replace('<<QUESTION>>', sentence)
                    prompt = prompt.replace('<<SUMMARY>>', pedaco)
                    prompt = prompt.encode(encoding='UTF-8', errors='ignore').decode('UTF-8')
                    summary = consulta_analise(prompt)
                    event.wait()  # aguarda o sinal para continuar
                    event.clear()  # limpa o sinal para a próxima iteração
                    text = summary['message'].strip()  # pega somente o conteúdo da mensagem sem o conversation_id
                    text = re.sub('\\s+', ' ', text)  # substitui todas as ocorrências de um ou mais espaços em branco
                    #                                   por um único espaço em branco
                    #   filename = '%s_gpt3.txt' % time()
                    #   with open('gpt3_logs/%s' % filename, 'w') as outfile:
                    #       outfile.write('PROMPT:\n\n' + prompt + '\n\n==========\n\nRESPONSE:\n\n' + text)
                    print('\n\n\n', count + 1, 'of', len(sentences), ' - ', text)
                    result_analise.append(sentence + '\n' + ':' + '\n' + text)
                    count += 1
            cont += 1
        else:
            print('realizando analise simples...')
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
                result_analise.append(sentence + '\n' + ':' + '\n' + text)
                count += 1

    def processa_resumo(data_hora_formatada, pos_inicial_resumo):
        algoritimo_summary(pos_inicial_resumo)  # apontar o último pedaço resumido de maneira a recomeçar pelo seguinte
        titulo_resumo = tituloDoc + '_RESUMO_' + '[' + data_hora_formatada + ']' + '.txt'
        save_file('\n\n'.join(result), 'repositorio/' + titulo_resumo)
        time.sleep(2)  # aguarda salvar o arquivo em disco

    def processa_analise(data_hora_formatada, num_carcteres):
        titulo_resumo = tituloDoc + '_RESUMO_' + '[' + data_hora_formatada + ']' + '.txt'
        algoritimo_analisis(open_file('repositorio/' + titulo_resumo), open_file('questions.txt'), num_carcteres)
        titulo_analise = tituloDoc + '_ANALISE_' + '[' + data_hora_formatada + ']' + '.txt'
        save_file('\n\n'.join(result_analise), 'repositorio/' + titulo_analise)

    def unir_resumo_analise(data_hora_formatada):
        titulo_resumo = tituloDoc + '_RESUMO_' + '[' + data_hora_formatada + ']' + '.txt'
        titulo_analise = tituloDoc + '_ANALISE_' + '[' + data_hora_formatada + ']' + '.txt'
        with open('repositorio/' + titulo_resumo, 'r', encoding='utf-8') as f1, open(
                'repositorio/' + titulo_analise, 'r', encoding='utf-8') as f2:
            conteudo_arquivo1 = f1.read()
            conteudo_arquivo2 = f2.read()

        with open('repositorio/' + tituloDoc + '_RESUMO_ANALISE_' + '.txt', 'w') as f3:
            f3.write('RESUMO_' + tituloDoc + '[' + data_hora_formatada + ']' + '\n\n' + conteudo_arquivo1 + '\n\n\n')
            f3.write('ANALISE_' + tituloDoc + '[' + data_hora_formatada + ']' + '\n\n' + conteudo_arquivo2)

    def processamento_completo(pos_inicial_resumo, num_carcteres_analise):
        tempo_atual = time.time()
        data_hora_formatada = time.strftime('%d%m%Y_%H%M%S', time.localtime(tempo_atual))
        processa_resumo(data_hora_formatada, pos_inicial_resumo)
        processa_analise(data_hora_formatada, num_carcteres_analise)
        unir_resumo_analise(data_hora_formatada)

    def processamento_1etapa(pos_inicial_resumo):
        tempo_atual = time.time()
        data_hora_formatada = time.strftime('%d%m%Y_%H%M%S', time.localtime(tempo_atual))
        processa_resumo(data_hora_formatada, pos_inicial_resumo)

    def processamento_2etapa(data_hora_formatada, num_carcteres):
        processa_analise(data_hora_formatada, num_carcteres)
        unir_resumo_analise(data_hora_formatada)

    def processamento_3etapa(data_hora_formatada):
        unir_resumo_analise(data_hora_formatada)

    #  Executa o programa
    try:
        processamento_completo(0, 0)
        #  processamento_1etapa(15)
        #  processamento_2etapa('14032023_171735', 0)
        #  processamento_3etapa(data_hora_formatada)

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
