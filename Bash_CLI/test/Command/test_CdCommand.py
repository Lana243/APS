from src.Controller import Controller
from src.Command import CdCommand, LsCommand
from src.Token import Token

import os


def test_cd_command_run_1():
    controller = Controller()
    command = CdCommand()
    stdout, error_message, status = command.run('', controller)
    assert status == 0
    assert error_message == ""
    assert os.getcwd() == os.path.expanduser("~")


def test_cd_command_run_2():
    """WARNING: To run this test use project root as a working directory"""
    controller = Controller()
    command1 = CdCommand(args=[Token("resources", "", "")])
    stdout, error_message, status = command1.run('', controller)
    assert status == 0
    assert error_message == ""
    command2 = LsCommand()
    stdout, error_message, status = command2.run('', controller)
    assert status == 0
    assert error_message == ''
    assert set(stdout.split('\n')) == {'subdirectory', 'a.txt', 'b.json'}


def test_cd_command_run_3():
    """WARNING: To run this test use project root as a working directory"""
    controller = Controller()
    filepath = os.path.join(os.getcwd(), 'resources', 'subdirectory')
    command = CdCommand(args=[Token(filepath, "", "")])
    stdout, error_message, status = command.run('', controller)
    assert status == 0
    assert error_message == ""
    assert os.getcwd() == filepath
