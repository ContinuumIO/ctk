from unittest import TestCase
import ctk.cli as cli
from ctk.cli import extract_command_args_and_kwds


class TestCLIFunctions(TestCase):

    def test_extract_command_args_and_kwds(self):
        # you must have a program name
        with self.assertRaises(IndexError):
            _args = []
            (args, kwds) = cli.extract_command_args_and_kwds(*_args)
        # you don't have to specify modules, in which case you return None
        program_name = 'program'
        _args = [program_name]
        (args, kwds) = cli.extract_command_args_and_kwds(*_args)
        assert args == [], (args, [])
        assert program_name == kwds['program_name'], (program_name, kwds)
        assert kwds['module_names'] is None, (None, kwds)
        # example of a full parse
        args_part = range(3)
        program_name = 'program'
        module_names = ['module1', 'module2', 'module3']
        _args = [program_name] + [','.join(module_names)] + args_part
        (args, kwds) = cli.extract_command_args_and_kwds(*_args)
        assert args == args_part, (args, args_part)
        assert program_name == kwds['program_name'], (program_name, kwds)
        assert module_names == kwds['module_names'], (module_names, kwds)
