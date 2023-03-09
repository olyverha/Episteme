from pyChatGPT import ChatGPT
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    while True:
        # session_token = input('Please enter your session token: ')

        token = """eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Ar67zvEFB4K-NIhW.9U0ToMCAMy-mPcqTszMEEmoIpU-5iA_nk0ekapNd4gnQ-49yNvFxCOgxKg0yVW5O8JXo2VhSA24sDHz7FboSBcPw93r9Uc9Xw-QI-qsJQYjHFqXHM1PMEW7EB720hBw2Fx7tgK7T-CfXBcNYliWzuF29WClO8btN7xR-nW2wNm7tNvNCSTASEgHw_9PUBh7DN27FA05svPY2Y2Epv-lDTkqZBwp1CstQh-tTxSS8ht16HpVF9y4LhapD0T6zCJkK6rL7TNRsVRIFpubONxcWTELGWGkMHJ2goQPlHGDE6djHDqDP_UN6vzaHRTgj369QPykpwGpEsqueHWoRWZtsHyYPDkTbtk8XBHO8bvpShu50M1tAMvEpuiRKj_fpGUNjZDFOaPnp1gpreyuFP6yFEc_excyENu-qlMzQcefowl9zsYIalBHqTVUfYBOn6Sr9lZYhVePpQJdbSXOUEbIeAqSKtomA3QwslqODBRlU6jRUbcAMni989179F9fF3esKilUBf76Jds65ofdQHr1ChlXpGO9wQ3khXA-F2LRLboRnOH1TtIJnTU1rmPTVzsrqdtnwCCDuhhw_zjqrERDbe-Sh1mJvboX7lYLMBoV46c47syrW0tSTO4RsyvAqbOX2gSHIll8vzC8BBs4W01sPp7ch1uD2LL13QZqWRRXDJA1TrcwZ_I7OSo4PfH8G0ndiFQ6_lhQNa4UaL2rGbhiHYgA0Q5lnnBEWYhCLz7i3LVwQOjaKJsFT2D7C4iYgkiqa6PPmj43pRIJE78sp59HNr-SDxhjDa4OuSkb7q5BmKX9AYU0vysTAajTw_fq3Imqlm6k0jb1kX2250oNoj16Agd4a4a5zOWSTYNrrkyV0ZCzmhG_7APr1AUA-ZGP6tw0_XeO6aOQ4xrOC5neHKut8AXPZ_X5FdtAFHDHSZAriLlYYQNXmYFe7PLbfLUojnXY8pNLQy0pW2rM7srTEoV5vCWNIaEsyETh3XA2VVLj42Zm_-gHgqSpC6C1k7bAU6GcvKiy-Qscm_2fFVd9VMXeX4TF-NjBC2d7gx2z0QcqIETSzMZ0E8X74baKU_2ZTAUMACtZQQilURZlj2dKb_3v_YlkpoDa-tnGZJ9ZmQMF4DRaxyTA6ukFcBlOTQ7iIavLERQoviI1-_dA4sPNHBxZOkcyor4rqJydOxGWHjDBNbWU8F_COL4lVk-I3qyaFtL6xIRgOgVtVgxaGvhN7oPY5u0TVFL7hZrORBIaa-Z33MGHJ74QoKHo85VvMSFa7WcpZHNge2cGyo_X6OF2qvCnZuXgQ5rOxKY9VoO1IVF87ByLHl8AYwBXLSSlSiPO2ecw-VT-8whpim3umjJf3CzFbsSH4nX6f6P-XET8G16Xq13a3vD83suSL_WklnAzOu8jcNtFroKF2zY_6_1gJYlCsFP-gn0PfGQByL_NhkkJucuDc_g5sQQCkUdhG61idrWMKWXu3LYf-luh80_2sdxOEhv5fnG0nR_m410PpOowOaFxpg_ffLqX5o_ouqiG1Ycmym_3a7uWs-yToEZuH9VUD5go1Ud0rGvJrUXAKWJw4jp9Wqu0__WRnLjtpoF06D1Xb2X1omlsxbYxuVEnHh2E_rNPshjlPxvIFDE4NpsgwdVaXIddKcr60d0kneUbq1s8Jy-00a32syqXmQ3ZZ90jSSqBvaW5F-F_jsXO4pfmzMPqyMzyYKIUnKaPO5EnaN5EKtdOEyYnGBKSEmcbvgUapGIww8t1TmJTgNyfIO2bCRB5k7-qkBs5way-vf1iC36EmD0j7ULAWKmDsMjXSgiYYxZxp3Ts5jG-ShT2kMCxOEkVN8K_v2VE0hCFCEGWFMX_sX9enPR_VvQTDbSqrO4978zE2Xz3vcu4hmXeOVqNbQi8XGfAby9nq8oApGBUPWEpcVOg58I7wfcNwUsdMbjD_4Fk8YTLDZO-ksYB7J_4espedyHGR7iF-3ZI44DFIa45_drTpfsRWeIB7ypyg48IbwKbz7cz-GV2ZwNc1GoxNDrwEyNHFFl8AcyGV5VvonUv784Hu_U0Y1rn0-0b4EdorXP3dfIu7gTNX1kdAfrKXWZIYO3WNqbMwx-QTbtWsMyz6yn55s63x96qfIyTCQejs3wwNEf2lZahxoSK5MsRfvpQko-hDiR1u2G7mKuW2xua6hWWXKYpKcFIvC4t9EBpJIGEUZwz5AToWek0EJ4uGJF6B0f1nT0yGcGEucYGw90y0yEM-pIgdRz2hI76EIYJ7ap1VgbaLWIJQWtf3FkhKUufai6FIwDlZEQ_cYod7-1ciiuFgUdn8SDEAqUZuJdLuN6qwzb3g6OKX6B6m14HVOypzsWgY4O5n741ET58UwWiFu19siWkWRDcG4B9PwIvWO3Km7stn6fJhj-uTnsjMC1XRKarB9MOC1XXqOyKaMk33pY0qtqozy1N-ZM0pr9u9km4k8Gj6nTfz4p6uMhaA3krbwF3TzwgiROQhX2QsgD8JluKsAaVNBSM6FbIS9cViKILfsaegfwJ1AeehkU6-BXmHa0MxzRNUtuk3N1NVMvF7H48tSNk9f8BTHidacPETwXOk5r2pq_iHmosjWTOlir--1YmFgWcb4KCABw0tC_WJMIV-2yzvFCyINYETEBXxFK0sttIJGKg5OAza1RxKVBxu2XKqFOp1yg.V6AFJ2EyKsaHzOdkWsbtHA"""

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
