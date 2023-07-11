import unittest
from module import unique_character


class UniqueTestCase(unittest.TestCase):
    def test_unique(self):
        unique = unique_character("""The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming""")
        self.assertEqual(unique, "m")

    def test_no_unique(self):
        unique = unique_character("Оох оохх Ооох")
        self.assertEqual(unique, "У тексті немає унікальних літер!")

    def test_characters_and_doubles_unique(self):
        unique = unique_character("'sdssdd sffs00 92 984jfjf llss@@@' ;@ 'ss ;d;d ;s;s aa asddsa qwqw dd || | ")
        self.assertEqual(unique, "У тексті немає унікальних літер!")


if __name__ == '__main__':
    unittest.main()
