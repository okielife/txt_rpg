from txt_rpg.characters.base import CharacterBase


class NonPlayableCharacterBase(CharacterBase):
    def playable(self) -> bool:
        return False
