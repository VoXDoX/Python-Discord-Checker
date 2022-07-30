from colorama import Fore
from os import system
from threading import Thread
from time import sleep

from utils import DiscordAPI


class CheckerTokens:
    def __init__(self):
        self._MODE_ = 1
        self._TASK_: int = 1

        self.bad: int = 0
        self.good: int = 0
        self.limited: int = 0

    @staticmethod
    def getTitle() -> None:
        print(fr"""{Fore.BLUE}

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╭━━━┳╮╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮
╰╮╭╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃┃╭━╮┃┃╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╭╯┃
╱┃┃┃┣┳━━┳━━┳━━┳━┳━╯┃┃┃╱╰┫╰━┳━━┳━━┫┃╭┳━━┳━╮╭╮┣╮┃
╱┃┃┃┣┫━━┫╭━┫╭╮┃╭┫╭╮┃┃┃╱╭┫╭╮┃┃━┫╭━┫╰╯┫┃━┫╭╯┃╰╯┃┃
╭╯╰╯┃┣━━┃╰━┫╰╯┃┃┃╰╯┃┃╰━╯┃┃┃┃┃━┫╰━┫╭╮┫┃━┫┃╱╰╮╭╯╰╮
╰━━━┻┻━━┻━━┻━━┻╯╰━━╯╰━━━┻╯╰┻━━┻━━┻╯╰┻━━┻╯╱╱╰┻━━╯
                                                by VoXDoX{Fore.RESET}
Софт был сделан специально для моего github (https://github.com/VoXDoX)
Telegram Channel: https://t.me/End_Soft
Owner Link: https://t.me/The_VoX
""")

    def checkOneToken(self, token: str) -> None:
        status = DiscordAPI(token=token).getValid()

        if status == 401:
            print(f"{Fore.RED}[BAD: {status}] Невалид | {token}")
            with open(file="./results/accs-invalid.txt",
                      mode="a",
                      encoding="UTF-8") as file:
                file.write(token + "\n")
            self.bad += 1

        elif status == 403:
            print(f"{Fore.YELLOW}[LIMITED: {status}] Ограничен | {token}")
            with open(file="./results/accs-limited.txt",
                      mode="a",
                      encoding="UTF-8") as file:
                file.write(token + "\n")
            self.limited += 1

        else:
            print(f"{Fore.GREEN}[SUCCESS: {status}] Валид | {token}")
            with open(file="./results/accs-valid.txt",
                      mode="a",
                      encoding="UTF-8") as file:
                file.write(token + "\n")
            self.good += 1

    def checkingTaskToken(self, token: str) -> None:
        discord = DiscordAPI(token=token)

        if discord.getValid() == 401:
            print(f"{Fore.RED}[BAD: {discord.getValid()}] Невалид | {token}")
            with open(file="./results/accs-invalid.txt",
                      mode="a",
                      encoding="UTF-8") as file:
                file.write(token + "\n")
            self.bad += 1

        elif discord.getValid() == 403:
            print(f"{Fore.YELLOW}[LIMITED: {discord.getValid()}] Ограничен | {token}")
            with open(file="./results/accs-limited.txt",
                      mode="a",
                      encoding="UTF-8") as file:
                file.write(token + "\n")
            self.limited += 1

        else:
            print(f"{Fore.GREEN}[SUCCESS: {discord.getValid()}] Валид | {token}")
            with open(file="./results/accs-valid.txt",
                      mode="a",
                      encoding="UTF-8") as file:
                file.write(token + "\n")
            self.good += 1

            status = discord.getInfoToken()
            if status:
                cards = discord.getCards()
                with open(file="./results/info-accs-tokens.txt",
                          mode="a",
                          encoding="UTF-8") as file:
                    string = f"{token} | username: {status[0]} | phone: {status[1]} | " \
                             f"email: {status[2]} | mfa: {status[3]} | verified: {status[4]} | nitro: {status[5]} | Cards: {cards}\n"
                    file.write(string)
            else:
                print(f"Не получилось собрать информацию: {token}")

    def startChecker(self):
        self.getTitle()
        print(f"\n{Fore.YELLOW}Имеется два режима работы:\n"
              f"{Fore.RED}[1]{Fore.YELLOW} Прочекать токен\n"
              f"{Fore.RED}[2]{Fore.YELLOW} Проверить файл (tokens.txt)")
        self._MODE_ = input(f"{Fore.GREEN}Введите режим: ")

        if self._MODE_.isdigit():
            if int(self._MODE_) == 1:
                token: str = input("Введите токен: ")
                self.checkOneToken(
                    token=token
                )
                collect: str = input("Собрать информацию о токене? (y/n): ")
                if collect.startswith("y"):
                    print("Ожидайте...")
                    discord = DiscordAPI(token)
                    status = discord.getInfoToken()

                    if status:
                        card = discord.getCards()
                        with open(file="./results/info-accs-tokens.txt",
                                  mode="a",
                                  encoding="UTF-8") as file:
                            string = f"{token} | username: {status[0]} | phone: {status[1]} |  email: {status[2]} |" \
                                     f" mfa: {status[3]} | verified: {status[4]} | nitro: {status[5]} | Cards: {card}\n"
                            file.write(string)
                        print("SUCCESS: " + string)
                    else:
                        print(f"{Fore.RED}Не получилось собрать информацию :(")
                else:
                    print(f"{Fore.RED}Хорошо, покеда :)")
            else:
                with open(
                        file="tokens.txt",
                        mode="r",
                        encoding="UTF-8") as file:
                    for token in file:
                        self.checkingTaskToken(token.split("\n")[0])
        else:
            print(f"{Fore.RED}Ты даун! Возвращаемся назад!")
            system("cls")
            self.startChecker()


if __name__ == '__main__':
    CheckerTokens().startChecker()
