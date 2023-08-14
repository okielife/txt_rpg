from txt_rpg.characters.playable.base import PlayableCharacterBase


class CharacterA(PlayableCharacterBase):
    def name(self) -> str:
        return "Character A"
