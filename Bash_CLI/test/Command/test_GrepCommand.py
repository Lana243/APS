from src.Controller import Controller
from src.Command import GrepCommand
from src.Token import Token


def test_grep_command_run_1():
    controller = Controller()

    input_text = 'a b c'

    command = GrepCommand(args=[
        Token('a', '', ''),
    ])

    stdout, _, _ = command.run(input_text, controller)

    assert stdout == input_text


def test_grep_command_run_2():
    controller = Controller()

    input_text = 'a b c\nd e f'

    command = GrepCommand(args=[
        Token('a', ' ', ''), Token('-A', ' ', ''), Token('1', '', ''),
    ])

    stdout, _, _ = command.run(input_text, controller)

    assert stdout == input_text
