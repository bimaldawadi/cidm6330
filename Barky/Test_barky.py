import unittest

from barky import Option, get_bookmark_id_for_deletion, get_user_input, option_choice_is_valid

class TestBarky(unittest.TestCase):
    def test_choose(self):
        self.assertEqual(1,1)
    def test_str(self):
        option =  Option('Edit a bookmark','E','None')
        expected = 'Edit a bookmark'
        actual = option.name
        self.assertEqual(expected,actual)

    def test_option_choice_is_valid(self):
        choice = 'E'
        option = Option('Edit a bookmark', 'E', 'None')
        actual = option_choice_is_valid(choice, option)
        self.assertEqual(choice, actual)

    def test_get_user_input(self):
        label = 'Edit a bookmark'
        actual = get_user_input(label, True)
        self.assertEqual(label, actual)

    def test_get_bookmark_id_for_deletion(self):
        value1 = get_user_input("Enter a bookmark ID to delete")
        value2 = get_bookmark_id_for_deletion()
        self.assertEqual(value1, value2)

    