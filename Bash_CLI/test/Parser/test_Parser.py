import src.Parser.Parser as Parser
import src.Controller.Controller as Controller

def test_parse_commands_1():
    controller = Controller()
    parser = Parser(controller)

    list_tokens = ['cat', 'aga', 'aboba', '|', 'wc', "'#x&y'"]
    assert parser.parse_commands(list_tokens) == [['cat', 'aga', 'aboba'], ['wc', '#x&y']]

def test_parse_commands_2():
    controller = Controller()
    parser = Parser(controller)

    list_tokens = ['echo', 'go']
    assert parser.parse_commands(list_tokens) == [['echo', 'go']]

def test_parse_commands_3():
    controller = Controller()
    parser = Parser(controller)

    list_tokens = ['pwd', '"', 'home/user/home = ab', '"', '"', 's=t', '"', '-v']
    assert parser.parse_commands(list_tokens) == [['pwd', 'home/user/home = ab', 's=t', '-v']]

def test_parse_commands_4():
    controller = Controller()
    parser = Parser(controller)

    list_tokens = ['cat', "'$x$y = $exit'"]
    assert parser.parse_commands(list_tokens) == [['cat', '$x$y = $exit']]

def test_parse_commands_5():
    controller = Controller()
    parser = Parser(controller)

    list_tokens = ['abc', '\'"raz, dva"\'', '"', " ' aaaa ' hhhhh ' ", '"', "' fffff"]
    assert parser.parse_commands(list_tokens) == [['abc', '"raz, dva"', ' \' aaaa \' hhhhh \' ', '\' fffff']]

def test_parse_commands_6():
    controller = Controller()
    parser = Parser(controller)

    list_tokens = ['x', '=', 'ex', '|', 'y', '=', 'it', '|', '$x', '$y']
    assert parser.parse_commands(list_tokens) == [['x', '=', 'ex'], ['y', '=', 'it'], ['$x', '$y']]

def test_parse_commands_7():
    controller = Controller()
    parser = Parser(controller)

    list_tokens = ['$x', '\'aboba$y\'', '"', '$x', '$y', '"', '\'"$r\'', '=', '15']
    assert parser.parse_commands(list_tokens) == [['$x', 'aboba$y', '$x', '$y', '"$r', '=', '15']]

def test_parse_commands_8():
    controller = Controller()
    parser = Parser(controller)

    list_tokens = ['wc', '|', 'cat', '"', ' | echo ', '$___12', '"', '\' x=ex | $123 \'', '|', 'pwd', '"', '|', '"']
    assert parser.parse_commands(list_tokens) == [['wc'], ['cat', ' | echo $___12', ' x=ex | $123 '], ['pwd', '|']]
