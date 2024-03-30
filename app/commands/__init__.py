from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        """
        Abstract method to be implemented by concrete command classes.
        """
        pass

class NoSuchCommandError(Exception):
    """
    Custom exception raised when attempting to execute a non-existent command.
    """
    pass

class CommandHandler:
    """
    Class responsible for registering and executing commands.
    """
    def __init__(self):
        """
        Initialize the command handler with an empty dictionary to store commands.
        """
        self.commands = {}

    def register_command(self, command_name: str, command_class):
        """
        Register a command with the handler.

        Args:
            command_name (str): Name of the command.
            command_class: Class representing the command.
        """
        self.commands[command_name] = command_class

    def execute_command(self, command_name: str, *args):
        """
        Execute the specified command with optional arguments.

        Args:
            command_name (str): Name of the command to execute.
            *args: Optional arguments to pass to the command's execute method.
        """
        try:
            command_class = self.commands[command_name]
            command_instance = command_class()
            command_instance.execute(*args)
        except KeyError:
            raise NoSuchCommandError(f"No such command: {command_name}")
