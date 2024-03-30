from app.commands import Command

class DivisionCommand(Command):
    def execute(self, args):
        """
        Execute the division operation.

        Args:
            args (list): List of arguments containing numbers to divide.

        Returns:
            float or None: Result of the division operation if successful, None if division by zero occurs or if no arguments are provided.
        """
        if args:
            try:
                num1 = float(args[0])
                num2 = float(args[1])
                if num2 == 0:
                    print("Error: Division by zero")
                    return None
                return num1 / num2
            except ValueError:
                print("Error: Invalid input. Please provide valid numbers.")
        else:
            print("Error: Nothing to divide")
        return None
