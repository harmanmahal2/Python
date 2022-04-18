import unittest


def get_formatted_name(first, last):
    full_name = first + " " + last
    return full_name.title()


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted = get_formatted_name('harman', 'mahal')
        self.assertEqual(formatted, 'Harman Mahal')

    def test_middle(self):
        formatted = get_formatted_name('harman', 'mahal')
        self.assertEqual(formatted, 'Harmanjot Singh Mahal')

if __name__ == '__main__':
    unittest.main()

