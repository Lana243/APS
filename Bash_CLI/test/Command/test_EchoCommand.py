from src.Controller import Controller
from src.Command import EchoCommand


def test_echo_command_run_1():
    controller = Controller()

    input_text = 'Aboba'

    command = EchoCommand(args=[input_text])

    stdout, _, _ = command.run('', controller)

    assert stdout == input_text + '\n'


def test_echo_command_run_2():
    controller = Controller()

    text1, text2, text3 = 'Aboba', 'boba', 'abobo'

    command = EchoCommand(args=[text1, text2, text3])

    stdout, _, _ = command.run('', controller)

    assert stdout == f'{text1} {text2} {text3}\n'