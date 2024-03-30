from app.commands import Command

class AdditionCommand(Command):
    """
    Command class for performing addition operation.
    """
    def execute(self, args):
        """
        Execute the addition operation.

        Args:
            args (list): List of arguments containing numbers to add.

        Returns:
            float: Result of the addition operation.
        """
        if args:
            a = float(args[0])
            b = float(args[1])
            return a + b
        else:
            print("Nothing to add")
