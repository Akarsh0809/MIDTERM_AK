from app.commands import Command

class DivisionCommand(Command):
    """
    Command class for performing division operation.
    """

    def execute(self, args):
        """
        Execute the division operation.

        Args:
            args (list): List of arguments containing numbers to divide.

        Returns:
            float: Result of the division operation.
        """
        if args and len(args) >= 2:
            try:
                numerator = float(args[0])
                denominator = float(args[1])
                if denominator != 0:
                    return numerator / denominator
                else:
                    print("Error: Division by zero")
            except ValueError:
                print("Error: Invalid input. Please provide valid numbers.")
        else:
            print("Error: Insufficient arguments. Provide two numbers to divide.")
