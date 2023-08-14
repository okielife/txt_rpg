from unittest import TestCase

from txt_rpg.characters.nonplayable.base import NonPlayableCharacterBase


class TestNonPlayableCharacterBase(TestCase):
    def test_abstract_interface(self):
        npc = NonPlayableCharacterBase()
        with self.assertRaises(NotImplementedError):
            npc.name()

    def test_concrete_interface(self):
        npc = NonPlayableCharacterBase()
        self.assertFalse(npc.playable())
