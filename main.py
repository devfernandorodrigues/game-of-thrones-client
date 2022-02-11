from typing import List
from schemas import Character, House, Quote

import requests


class GameOfThronesClient:
    ENDPOINT = "https://game-of-thrones-quotes.herokuapp.com/v1"

    def random_quote(self) -> Quote:
        resp = requests.get(f"{self.ENDPOINT}/random")
        return Quote(**resp.json())

    def random_quote_list(self, quantity=5) -> List[Quote]:
        resp = requests.get(f"{self.ENDPOINT}/random/{quantity}")
        return [Quote(**data) for data in resp.json()]

    def quote_from_character(self, character: Character) -> Quote:
        resp = requests.get(f"{self.ENDPOINT}/author/{character.slug}")
        return Quote(**resp.json())

    def quote_list_from_character(
        self,
        character: Character,
        quantity=5,
    ) -> List[Quote]:
        resp = requests.get(
            f"{self.ENDPOINT}/author/{character.slug}/{quantity}"
        )
        return [Quote(**data) for data in resp.json()]

    def houses(self) -> List[House]:
        resp = requests.get(f"{self.ENDPOINT}/houses")
        return [House(**data) for data in resp.json()]

    def house_by_slug(self, slug) -> House:
        resp = requests.get(f"{self.ENDPOINT}/house/{slug}")
        data = resp.json()
        return House(**data[0])

    def characters(self) -> List[Character]:
        resp = requests.get(f"{self.ENDPOINT}/characters")
        return [Character(**data) for data in resp.json()]

    def character_by_slug(self, slug) -> Character:
        resp = requests.get(f"{self.ENDPOINT}/character/{slug}")
        data = resp.json()
        return Character(**data[0])
