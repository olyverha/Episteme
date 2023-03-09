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
    alltext = open_file('input_completo.txt')
    chunks = textwrap.wrap(alltext, 2000)
    result = list()
    count = 0
    while True:
        token = """eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..JZRMSpXm1OJ - KjDA.3OwzdV44zk7K2P44JeVK1zj0QwEnWI - uI37MW8GojOr3nTMiX1lGVVZ5NIowU2JtWr_a7CkNhSZHzX8yaccb_YKSujDy - AdEuKihBCXGLRPOe67fnkU5Bjjv - A4Ue5zrcWwQKng4oow6c3vyKB2 - q5Gn7_2xVMXwevXcQW6IHCHhhhEasmuSpCYljdFCqypaTHBG4cLpye3B - 9
        zfQlvOJez4IzKK11Lxr1ubx1r7TnIeWb88ekBcPyAb7PZOxi6AgqfeWr6oUjHO4YLSrvEgpP8Hpwck8ejHTaxS7zw6wP22z47sJkqaRW1K4NJftbDpBoHRWk189Rs3Ojqh5IcnsOh2Gq2V5WchhMSiTCpLMH48J5pg - sWgbVkt5flP0HP72CegiCtAaOU6iSkPy4rAv_kiP0UIKuvdfNTpjkRHlUXkgOZIqpHiUjOVN31ZgUeDwXLpSxcfRc4afpp4J8VfiIPbZxwKTVfmS9XxpSeu7 - -56
        bb6rmZZLGcbCFxteDOX45iIlkkZ15PDtyya6530B6Q8txbFI7a5keVbB8mk9y_XoyvAP_zQSEG0vp6ukT6664yvl - dgNu - MKEBBbf7FtrwjBsnc4pwdfB1A - nfTx43jed - e7pAGHpAP6QOOOjiqBOs1wKY4jal1j7TnE4BrnOY2AjktTG_YTk7t_QcOIsQNePEvTAm7bfjcQ8DRuj3patpEDGt_jFeKDt9u8YoDCzIk08wnO1LI396SmgHSiKAAkzLVofJqLXbEqrfRzqX8SCXWhOwjxojEadyBulIH5WV8r1OoqhIy8 - 0
        tQg5MKuoy2DQati3P5_NxGyFyBsuyYM0JF6cI9xfMYb2OiZrydaEjo9LH9PwbwMqq1fuZS0XAFifMfBwnOVKqwk4M2R9VDnPzSo - YRRWp3OqYPICap9uGQSM71Z5jB8pNNTUBT5GC8EpmVXrpdJlJY5l08d953f - 3
        iF6ehORwYsUhcD3Q8FUZBP6V_YbG6rCP_KWQbhmRO - ZwUFZRJ5eJWk9CE0QL - fvBaoEalJaIISQ2APrkRwQWcviMIRMJiSwlSzRyvOta4khiAaiHJZXQH - TilqboOv9nws40PN6cL83LFeTENNeAk0YFZKEI_6S4pr01d2tsdbZrXLVUxLeSKBrx8ZklFSkWbxrXt6jqiEDmAMMLUpiP2y3jSIwYk8N6SP0YG5rUwajEcQrdB0E5P8VjLtf9eL3_0dEz - 8
        DJNH93s65sp57HOix3kLi7MYPXm8d_dhT - RJE4wIfQSubCBO4zYIXkggaAN_HjeN2 - 7Tf531_VncIB2IHZ4ugix45Yw8_ - x3Ae0etXkXGwDrfCBzg3bLmfESEGvSECzK3gUKbTMBBe6PuhNYT9VcovzwZbWtgX7z4c4FxinkF0HXfwRRjfi4eUQFNff4TGzHoNVrQ_rFrXRPdXcjmMMsjdrQWuLBRMfgfqbxywysrZsDLnmy7pieXecorGinsfzmrMXAqvnao5TiL1W29V3ifd2b7kBhIEkyt6UOd1tQecA1Gql9mpPDp1jHNJBAgVdqxyg6ScezijII0YM377ye2111N5ZycmfkBmshRcpKA8mLrhFRsN18tTbe - k5ILPk - vezndgdPbgCcam4DOxoQeinaE5a9Mjh8a02SjGvsNYjiQysAi1wKe2zJvobrdqzeh05pT50tzJCvWMNrqEfQos1HFOzMAKOx - 3
        Ibp2W3p2d3ksW - nNNLBj7C - hqY17YU5qi2ZgR2s54foUGgM5PpJz3clOCDaUa8HEr4mShekN2eKAhwvjhoDdzSSvYbmN4B8_0cCfhXCUCtrRzGg8jVfbJsQcXLJqRF6kFdnecxdr30VFCrnsant5FpYkWMBKLSJQk6hnRQILYTwkP1xEHxBkIxrFP1ld6KSuhCTJwuV3sxjP8qJVO1baERiFgo70v7QcKzQDpU3yVOt7SMrNJzgNgwlBMqwsv - MclhfxLYmoClb7_XxAks9OWIUSeaPt8ThH7afu3xU0Xtx1gfHFY2xYP41s9awMELlje_0SMjWd6K3xhZ6S8I6g08PiJG0tny8bKSSsXHarTz29 - RHdWz_EKH20C5NYwGsbRCTfPq_nYkwWBl_0ya3YHCXHBD8f5yqvoSUhrGioe - 7
        xuxuyrolG9Szp2vPWYghaUZUiZ_yZh - ojGPoaF3oozVL - bNd9nUPBbq_iU8PyV7yV38NtCXjbEDMWLpsJzlLGTwJnVWfYsal_PBl0l7JBQEHOBOz02OBVKYrUUz1h6k1fXh6G2j7GZoXEtAQdLZOO7XM5vajU2nPu1nniwiCOvX1207nsmw9eEU5ZQuB8e8InKrm7FIhkxJb8zvuJvdVAy9ulgKiOPwjNwLsH - 6
        PEILZbr_AzLFez - k54osO9qcKjiMYk6bR318zB4cKkZKy8FATpGQsT1s13vzog - Oe7nhNR8oCZazD9By83_Bv_my2V9CO5V - 32WMe49Ld104ODiAyeQNnIw5iFm9n_zLjy16_98vohi3JK57Kgx4NhGJgLkK9X5KZMXblPOhdFrJnJEngkHzwpxQvodyoA4bEQYogd8UmOmvWzm6P8MZTXn5r9HcWGnVVpsIblwLj1KVUNa6NBHr6wcbZv1AQbwNV43xuVbRwWt - V1wOeih1gX9tM.tJ2RxPTeMsPxeeGPeQ9Hhw"""
        session_token = token.replace('\n', '')
        conversation_id = ''
        chat = ChatGPT(session_token, conversation_id)
        break
    clear_screen()
    print(
        'Iniciando o resumo do documento...\n'
    )
    try:
        event = threading.Event()


        def consulta(_prompt):
            resultado = chat.send_message(_prompt)
            event.set()  # envia o sinal para o event.wait() continuar
            return resultado


        for chunk in chunks:
            count = count + 1
            prompt = open_file('prompt.txt').replace('<<SUMMARY>>', chunk)
            prompt = prompt.encode(encoding='UTF-8', errors='ignore').decode('UTF-8')
            summary = consulta(prompt)
            event.wait()  # aguarda o sinal para continuar
            event.clear()  # limpa o sinal para a próxima iteração
            text = summary['message'].strip()  # pega somente o conteúdo da mensagem sem o conversation_id
            text = re.sub('\\s+', ' ', text)  # substitui todas as ocorrências de um ou mais espaços em branco por um
            filename = '%s_gpt3.txt' % time()  # único espaço em branco
            with open('gpt3_logs/%s' % filename, 'w') as outfile:
                outfile.write('PROMPT:\n\n' + prompt + '\n\n==========\n\nRESPONSE:\n\n' + text)
            print('\n\n\n', count, 'of', len(chunks), ' - ', text)
            result.append(text)

        save_file('\n\n'.join(result), 'output_%s.txt' % time())
    except seleniumexceptions.TimeoutException:
        save_file('\n\n'.join(result), 'output_%s.txt' % time())
    except IndexError:  # Erro:Too many requests in 1 hour. Try again later.
        print("Index Error")
