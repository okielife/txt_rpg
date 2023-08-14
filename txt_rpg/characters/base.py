class CharacterBase:
    def name(self) -> str:
        raise NotImplementedError()

    def playable(self) -> bool:
        raise NotImplementedError()
