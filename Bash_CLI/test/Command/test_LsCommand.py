from src.Controller import Controller

from src.Command import LsCommand

import os

from src.Token import Token


def test_ls_command_run_1():
    controller = Controller()
    command = LsCommand()
    stdout, error_message, status = command.run('', controller)
    assert status == 0
    assert error_message == ""
    assert len(os.listdir()) == len(stdout.split('\n'))


def test_ls_command_run_2():
    """WARNING: To run this test use project root as a working directory"""
    controller = Controller()
    filename = os.path.join(os.getcwd(), 'resources', 'subdirectory')
    command = LsCommand(args=[Token(filename, '', '')])
    stdout, _, _ = command.run('', controller)
    assert stdout == "poem.txt"


def test_ls_command_run_3():
    """WARNING: To run this test use project root as a working directory"""
    controller = Controller()
    command = LsCommand(args=[Token('resources', '', '')])
    stdout, _, _ = command.run('', controller)
    assert set(stdout.split('\n')) == {'subdirectory', 'a.txt', 'b.json'}
