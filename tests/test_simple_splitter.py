import unittest

ai_tests = [
    ("hello world", ["hello", "world"]),
    ("hello  world", ["hello", "world"]),
    ("hello, world", ["hello", "world"]),
    ("hello-world", ["hello", "world"]),
    ("hello_world", ["hello", "world"]),
    ("hello   world", ["hello", "world"]),
    ("hello\nworld", ["hello", "world"]),
    ("hello\tworld", ["hello", "world"]),
    ("hello,world", ["hello", "world"]),
    ("hello.world", ["hello", "world"]),
    ("hello;world", ["hello", "world"]),
    ("hello:world", ["hello", "world"]),
    ("hello!world", ["hello", "world"]),
    ("hello?world", ["hello", "world"]),
    ("hello'world", ["hello", "world"]),
    ("hello\"world", ["hello", "world"]),
    ("hello(world", ["hello", "world"]),
    ("hello)world", ["hello", "world"]),
    ("hello[world", ["hello", "world"]),
    ("hello]world", ["hello", "world"]),
    ("hello{world", ["hello", "world"]),
    ("hello}world", ["hello", "world"]),
    ("hello<world", ["hello", "world"]),
    ("hello>world", ["hello", "world"]),
    ("hello|world", ["hello", "world"]),
    ("hello\\world", ["hello", "world"]),
    ("hello/world", ["hello", "world"]),
    ("hello=world", ["hello", "world"]),
    ("hello+world", ["hello", "world"]),
    ("hello-world", ["hello", "world"]),
    ("hello*world", ["hello", "world"]),
    ("hello%world", ["hello", "world"]),
    ("hello^world", ["hello", "world"]),
    ("hello&world", ["hello", "world"]),
    ("hello~world", ["hello", "world"]),
    ("hello`world", ["hello", "world"]),
    ("hello@world", ["hello", "world"]),
    ("hello#world", ["hello", "world"]),
    ("hello$world", ["hello", "world"]),
    ("hello!world", ["hello", "world"]),
    ]
camel_split_tests = [
    ("helloWorld", ["hello", "World"]),
    ("helloWorld1", ["hello", "World1"]),
    ("hello1World", ["hello1", "World"]),
    ("hello1World1", ["hello1", "World1"]),
    ("hello1hjashdjagsjhdWorldAsasagasdhag1253672", ["hello1hjashdjagsjhd", "World", "Asasagasdhag1253672"]),
    ("1234", ["1234"]),
    ("", [""]),
    ("WWWW", ["W", "W", "W", "W"]),
    ("WwWwWwW", ["Ww", "Ww", "Ww", "W"]),
    ]
snake_split_tests = [
    ("hello_world", ["hello", "world"]),
    ("hello_world1", ["hello", "world1"]),
    ("hello1_world", ["hello1", "world"]),
    ("hello1_world1", ["hello1", "world1"]),
    ("hello1_hjashdjagsjhd_world_asasagasdhag_1253672", ["hello1", "hjashdjagsjhd", "world", "asasagasdhag", "1253672"]),
    ("1234", ["1234"]),
    ("", [""]),
    ("WWWW", ["WWWW"]),
    ("WwWwWwW", ["WwWwWwW"]),
    ]
kebab_split_tests = [
    ("hello-world", ["hello", "world"]),
    ("hello-world1", ["hello", "world1"]),
    ("hello1-world", ["hello1", "world"]),
    ("hello1-world1", ["hello1", "world1"]),
    ("hello1-hjashdjagsjhd-world-asasagasdhag-1253672", ["hello1", "hjashdjagsjhd", "world", "asasagasdhag", "1253672"]),
    ("1234", ["1234"]),
    ("", [""]),
    ("WWWW", ["WWWW"]),
    ("WwWwWwW", ["WwWwWwW"]),
    ]
title_split_tests = [
    ("Hello World", ["Hello", "World"]),
    ("Hello World1", ["Hello", "World1"]),
    ("Hello1 World", ["Hello1", "World"]),
    ("Hello1 World1", ["Hello1", "World1"]),
    ("Hello1 Hjashdjagsjhd World Asasagasdhag 1253672", ["Hello1", "Hjashdjagsjhd", "World", "Asasagasdhag", "1253672"]),
    ("1234", ["1234"]),
    ("", [""]),
    ("WWWW", ["WWWW"]),
    ("Ww Ww Ww W", ["Ww", "Ww", "Ww", "W"]),
    ]
class TestCaseSplitter(unittest.TestCase):
    def testcamel(self):
        from autoCase.wordSplitter.CaseSplitter import CamelSplitter
        for test in camel_split_tests:
            self.assertEqual(CamelSplitter(test[0]), test[1])
    def testsnake(self):
        from autoCase.wordSplitter.CaseSplitter import SnakeSplitter
        for test in snake_split_tests:
            self.assertEqual(SnakeSplitter(test[0]), test[1])
    def testkebab(self):
        from autoCase.wordSplitter.CaseSplitter import KebabSplitter
        for test in kebab_split_tests:
            self.assertEqual(KebabSplitter(test[0]), test[1])
    def testtitle(self):
        from autoCase.wordSplitter.CaseSplitter import TitleSplitter
        for test in title_split_tests:
            self.assertEqual(TitleSplitter(test[0]), test[1])
if __name__ == '__main__':
    unittest.main()
