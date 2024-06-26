from pyChatGPT import ChatGPT
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    while True:
        # session_token = input('Please enter your session token: ')

        token = """eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..X6oRTg9RuRZP7THl.BxVAEEUNDM0outPGNYov4NTosDzN1doDTz9yYqJdT3L8pA7R70J5IEd0_l5IS73ltlNFBk9jDtRW5mIV4Xg7CYebz67hIJlUuX4RLnNHVsl9xm-bTd16L5_ezKkbyReVli4cq7Tk9zvrNL2UVahJ43zaCimVFnVnDzYcjEL7LOcLNZLapTGm6V6PSoNkWISNk_GCn7S9R5Xgw9ZvWrCGfCixl_dm0Ahp2vBSm6Ocq5aWamV4aCiTBTGV-sDq0nu9dzU2BTXug5j8wmzqd4_rD6db_yz1XRWpCNcxZv3Gos7NDkTGbADQqswxmyyg1XdMeA2qrtqBsC_ITeDo5mo5r0CUgM7skPW2fvYXVntMqSRNuItX9l5RsbMPDAqOIkyYGqOMcOyC5nBu01uVee0GInJQGaiImBTiZxV9X3SnHrDenTrNJ9V3HXA9WYdT7QGn9TKuhvbKYLPG-8cdxLKxyL9Nc3k5Z7Q7jhFka---BicAQ5g62krsvyz2oZ6bchqwNJjVBj1URVn8X-3dPSoO50bfNnUBiVJkAVnmJFrwp4uLFPUSKmZHWkCOMFEASDbiUUJVciT9YYf-y27Ixg7eQWYyxW7PqIBlqyuixwCzhSqDqmb7JZ11-TEUiJMOZbK83IVcStxa61IggQ16XO2WnSRJP3iY5yY7AXcW-zxYO0ShVrSlegmKJaPSnYTB4GmzvSO_Zh7jUTUh5ezWSQlShNv_QxeJu_Mw_02qqlyoy7Ex170608UvLjqUWgg-tR9eVYvQ4fKAh_sUKquTJn60LqHiZJB42RJ6g-D6Y3B4qGQnpC_cftGQY0FX86CEn-YaYK67C5bxXOxpcc-0Y2AeExJoWNCs8dOpgh4Vj-Z57jebPTzQgxla9O2IanZtyTyMLTJIMoUycUMDrzsxV5kjPyfJCPFBL97DVCvO8FxzZzWtmkPmjcEFp2iv-sxrUp9vSTxRUlqS61wHQRnZFhuksxp8g-cUmcbJBdnB5N5ruUbzy09M7satCnx_3xQR9OBL9i-JYSBtuIkWoqvRF9CR4P9HTuEZ2Mv8qgsozx8ZZ5n-HHM76tLrNWSi4BHY991fJWY5xwsWby4UlRSSiyBXoJ3t8K_tf0uSiDddPRzRY0UoTOhq8y8FlMlvwKfaAxSDOaa_YgLFJZsgrwEBdy_lTTXZObSyS-ula0j7GngNg9Ip7b5ZFv5q-7gYbJq2zIfdlG7mxTXhBAcuAHvOAajRaV1GnWflh1GmaacpjtCVXtRXg1DiM-qLftpYQt-6X9FnIK3lixcSzGRn75dF79UbHrHNSIsiVjjIyAPCBoiPV70xQ1imFI4qIODHtWUkoRfAMVTr_8c0lEK2JXGyEHy49N5FOl9hmKO2-hVQ3A12-BrMTD2gRgazJqrBo6lU2yDEUtJwtYsOKaqkOyGO9OgKOwGlDVBk5JHTNmgJI8j8D-UVOi25wic2DSRSBvnvVBh-d1OmXzxRdmm_eOBHPHp7_zdvRZRIzv4C9Ea8YOMa-69_H_ykilBdGkxPpiICx9am1BDaaPa8Xfsf5jXIXpXl_RVhdWBCwq7bjhXAwHgoqS-KwP951Lcw7w_E0OTVjnhIbZCylChuzXlcWf3A9z4R-Ihb5LYM89Pi3sdebDcnHjl3FhIK4ZkYi1FvP20fhmfiYpfphvfPeXTh_AD-Bs-ozog6GszYcITbNaZPh_B0OryCv_nwvcDIn1ZdQMZfQXxZ1LOTkC2979AhfvdlDtnccA7-T0n70pAMBI2ttMBUbKwtvbNXOcDHIq7djp0evQt-A8Z1lTKnrgNFxN71gaRToxpGyJmMzQgXDY2ag9g_V4_GYQZbcLn3buEX_qKDV9O73uGvMABtwGuzrOkihkRt1-fhka98aqryh4fB5_5id6WLg0tDwN0UWDLABvSXNmrZGV-bloA6W9yvjgJXCcL_EYtofYvPWsukqX6R348WzSxPt612f3cuO9PMHBnOXl80GnpiXspS-4qmdlKkF9VaAVDMaQ7GpFq-H_HCRqjFWUx2OE_yV3iUQAM-TZY1jL-bel_ICrvoG1J7W6_HOUUNcnOXN50FRqcZbPpe7LbJjDXOlLVOA4bic-ULJFjVp0IsqMVeepwwkKZLs_p9gzYmqJIoWMc1orW0tnlYbLYKIPHQYHknu3hcgLqr5Kx-56t6WbSloxt9-WvpnP6QB01xq4c0jnJD5Pv1hCTey3sdbMG9l9Nks3By86S2iFqS7fsUkU92V9jR-6yxaBH4KfqEdw75dV4Y9_lnqUdjyq3G2fze6BycRbxmgln8UAh7rLyp6StrAfkLs_7Yvjz0IzvofZt01DgNoKqZQGKp1NTiAHg7MD-kh_1Vmwlm0J6oZJs8jxhcoUAbe98CE-g_M9y2Ia82JUbhIZYiXXTkeIqi_8CynG2WdziypPCXeigZweWN8XxrBbyAGncyIcdPHVfnsE7pgIZd4Gnmj4PowABiZ2GSqLyxZ48UW_SBzzZ-W8QBMlp7LSsTUKNQmk3SIOCiM16FHNcOkI_aPKVUZuv0pYMAfep3ghwxt_e6K-Xcoaqw9RH8zPfDe4XccpiY3PjhHJPochE06-XWpeuNn5Lf8GhTyvFqR5EXLgcV-Q12QBT9GBeNSrqwFVuYboqpRd4871oisW1lspv24OzbM0ZBiNo.6SGZaOxgn055htKpGJU5CA"""

        session_token = token.replace('\n', '')

        """
        conversation_id = input(
            'Please enter your conversation id (if you want to continue old chat): '
        )
        """

        conversation_id = ''
        chat = ChatGPT(session_token, conversation_id)
        break

    clear_screen()
    print(
        'Conversation started. Type "reset" to reset the conversation. Type "quit" to quit.\n'
    )
    while True:
        prompt = input('\nYou: ')
        if prompt.lower() == 'reset':
            chat.reset_conversation()
            clear_screen()
            print(
                'Conversation started. Type "reset" to reset the conversation. Type "quit" to quit.\n'
            )
            continue
        if prompt.lower() == 'quit':
            break
        print('\nChatGPT: ', end='')
        response = chat.send_message(prompt)
        print(response['message'], end='')
