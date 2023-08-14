from unittest import TestCase

from txt_rpg.characters.playable.base import PlayableCharacterBase


class TestPlayableCharacterBase(TestCase):
    def test_abstract_interface(self):
        pc = PlayableCharacterBase()
        with self.assertRaises(NotImplementedError):
            pc.name()

    def test_concrete_interface(self):
        pc = PlayableCharacterBase()
        self.assertTrue(pc.playable())
