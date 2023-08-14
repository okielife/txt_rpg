from txt_rpg.characters.base import CharacterBase


class PlayableCharacterBase(CharacterBase):
    def playable(self) -> bool:
        return True
