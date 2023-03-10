from time import time
from chromedriverChatGPT import ChatGPT
from selenium.common import exceptions as seleniumexceptions
import os
import textwrap
import threading
import re


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def open_file(filepath):
    with open(filepath, 'r', encoding='UTF-8') as infile:
        return infile.read()


def save_file(content, filepath):
    with open(filepath, 'w', encoding='UTF-8') as out_file:
        out_file.write(content)


if __name__ == '__main__':
    alltext = open_file('input.txt')
    alltext = re.sub('\\s+', ' ', alltext)
    chunks = textwrap.wrap(alltext, 2000)
    result = list()
    count = 0
    while True:
        token = """eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Z_2qw3OSrY1RawYO.2QgXjuB-uL2ipm5eEW6xFNrkXzqI5WDn_9sDrHVszkWll_EUocsr9Vpeab_V8rOYOvS6An4w-0Qoqy3kIA_01DRyjiNHmO43LxzZXj0FPqtm-8OKG68EP7N0yYq0Z0LWD3byuCURUEgYjOtnwDiqs2z93RfIqJb4wn-jqLeIrALbp15y5hVjPak2W7anWHMRDc_W4wpahzaAPy1hd_SEeObI1_cKFu-_ldVXvgSkIkU8qh8mWGxEtvN3C6nRJj-zatc1mHF8erZzYFvhW3B5TN0UCcowLrhGzWWKupR9YpSefa5dBNqpZFXnDQjnUD362UPWsJgbQgi7PkljqTKHs4nXTmZVyf7oGs0rc3b6I0bain3CZZlqnueD7_ACdO4qHNn8jfAinifTKgzaP5qKkZJBpJpzpkG5NIADfhSjyIxuhV10Jg8m_mvaw_evMe2M6J1qoAb-L42jqrQ8CZDiawx-Wt6lpZmoxzK_8KxxcEgP8EdnTOa_-DNrjUehO488jx_c83eVLhYz-RUawV6bJKt7lFdtbu0JSTy_C3V9SQVXH7rfLtIt8IfVFd3xP3N7638A0_Te8pBe0_TZgOHj-a6QRzsyWVj1QRK8XhWxhAOLChQ1cubWFD2q7INq97zu66Xer_Kof5oDpim0tBfoRZMmQuLq8k4Ye9pi4Br1wQ-ESX2I6VW0pzWvvBHviGA9h-kmcs1XApwkOcQi6UDXbuC-YNNs16ycWaHtQ9aXld6gDTjcy0cEokzoNClWbzj4qq6zwlPmq3xb8TlzHgcHfZZws2qHoLm9Il6aTCCMUXNXuUWtzij4Bgdgb6ztY830NhOZvtOSmthdP4arr70yQu_XY8ti6sjXm0D4X9shJGQLxq4dAWitpRN_75KqmtClZ9BpuPlxTX_Z4HC-pqNy1tGA3Hep5s7JIhyqPNSEeAQ_dZ3MUTW8mWSLDjll59TZ9Mgr9AxXWEJLMyLNrEkre2IRdDUBuLHbZX1Mn38s2MGfOs0q9SX18gaj7LdADs-2WD6fJYPUI1mtHsdL_rBXtapa4Rwq9Sgpaxe-YKHJ63RFQDaW5EM8DlXFyjLLfHs6vfopnMH2PebgKbYpHS5ArUc7HbAQFnwc06ig6Dl1mRU-NNh6x4hGs0Seud_i6ecSV5ttB5znfZfNd20dxudSfNIfl5OE7czQJ4YqOSFbAMFy4uCGFPm7hHxRLhk4kFo-XQ6SA-QmLH8alJzyoY_-FuKoDkGRQl7GX5oFyz0H43kBRmJMN_QIw_zGC9M_sr6a1sURJHKmME5GKuU3agFzVUH_-CZZrnljx6ql8dKOXNBNVVVn3Mr0yyTj0HccBG0d53nqj6TNAEUjFIgrEDM1fi20-Izm-RGqzrn-QKZKGGT6_rbTl561SW56sZph7B3wV3k9IwsMSUsMCxyJifNAWV12MBzAsFalAGBnJoMwLO0jSw1Tow_VQpeXS-MX8knFB-38IDqY9_NsiVhvtP_5DRhR0YVOjHgIu-wqQlRRk6Zt_JGUW1AcQq3PSeaSMXQFt__CXx7PUB7kM8Xk8Q5oE9zlTuEhR-qc0uy2m5B1PT-TDHzl_ie84PPWvc1OoeyPXiLB1S_s-AGDrSyEu2FrCWAhDwHbNfKdU__df7-ddWChScotd6Qt41LsBfdta-hV5hsNn7XV8MxG9i1ZXF_In_3cY6MBpxRxJTOXzGnobyz2YKp4gcWlmjFJRc40CMjtMzsOfb8mrfx1CGwyG31e0h7lQgX0T-WfEZ9HjSHV0pjb1QzqE4KY2dU6Vxd8wVQeKsYxkMUQ4kIyDqz61n9hTyY3nQLqD68wSPz7DVZ2wUTacAX8kzNbaj5FMHoxUadWLzUwu9aNRXArm6ODBnx2Mc9FxnjT2I08wRw26RrqgiafpbgJcuna6nkpnlgYDp1rM5fN9TDItP_TtXbW0nL27tUg2jZoG08BPCVJMfiUeXv7c_2ow-je2GyfAsimZKyGwVVqqty4kF2IjHYcb8wFeoc3Kjwy9Ce_ms10lQ_ElbJwT5QeUEtp3o3QVyYhxzfw9uETROB_qXdD74iES020VFC9Dq0cHAMmUuGheAeOVNwN0PtWXF1McIaiL04LtOhtepZX5bVXoTsdtCfHaBSLrryFUOUz_Jbf7e8elEtwBMvFT3U43rzp-MhTrk86FQKC7sYGBDC6v_g0bNBy6BS6wVqd7oN6TLH5zXj3ZEfegpB5tENzn2Y3M4C2X1aPvs1S9T03Grz-Y9TkDqcW7sBgMaXjVPVrS3lMopFLuoTlpiSVN2yVUjvOzxyHvvUS4fsS7c_oEF6rfWU30fKZj1KD5VgNDcDWc5fHiN8YcfHZqJXM7vbWiLGawg9z1MGSVowiYlf0Qp2vIZ-exKqD5itiI71XtgLSp9nDniPhACd-vWsKFy_zegYfFfzfXm9qX7zaaceGo1dM-mhf2kTmLupky9ynF_cyv0UEeOmVoPzlWhS_D7lhKtTgn4dLZnBDip5Gkz2QdR6LQJ35_FAjPPpfrxR9wzNEtq157rNP4QIGMlCCkX7rT1UarZTdDTwyOR8Km0VvQjBUSlEDINUNqAwl1yziUWRG9y0jtQA8Zst_YYWCH-KPVoMP7bS0vFEu-QQIKuMoFjHboR8mmiEh.aacRPCMsQN3kEgKUTZn70w"""
        session_token = token.replace('\n', '')
        conversation_id = ''
        chat = ChatGPT(session_token, conversation_id)
        break
    clear_screen()
    print(
        'Iniciando o resumo do documento...\n'
    )
    contador_geral = 0


    def algoritimo_consulta(cont):
        event = threading.Event()
        contador_interno = 0

        def consulta(_prompt):
            resultado = chat.send_message(_prompt)
            event.set()  # envia o sinal para o event.wait() continuar
            return resultado

        for chunk in chunks:
            global contador_geral
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
                filename = '%s_gpt3.txt' % time()  # um único espaço em branco
                with open('gpt3_logs/%s' % filename, 'w') as outfile:
                    outfile.write('PROMPT:\n\n' + prompt + '\n\n==========\n\nRESPONSE:\n\n' + text)
                print('\n\n\n', contador_geral + 1, 'of', len(chunks), ' - ', text)
                result.append(text)
                contador_geral += 1
                contador_interno += 1


    try:
        algoritimo_consulta(contador_geral)
        save_file('\n\n'.join(result), 'output_%s.txt' % time())
    except seleniumexceptions.TimeoutException:
        contador_geral += 1
        algoritimo_consulta(contador_geral)
        save_file('\n\n'.join(result), 'output_%s.txt' % time())
    except ValueError as v:
        if 'Too many requests in 1 hour' in v:
            print('Limite de consultas em uma hora atingida. Aguarde ou informe o session-token de uma conta '
                  'diferente.')
        elif 'Incorrect API key provided' in v:
            print('Incorrect API key provided: undefined. Erro de comunicação, tente novamente.')
        else:
            print(v)
