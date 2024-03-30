from app.commands import Command

class DivisionCommand(Command):
    def execute(self, args):
        """
        Execute the division operation.

        Args:
            args (list): A list containing two numeric arguments for division.

        Returns:
            float: The result of the division operation.

        Raises:
            ZeroDivisionError: If the second argument is zero.
        """
        if args:
            # Convert arguments to floats
            a = float(args[0])
            b = float(args[1])
            try:
                # Perform division
                result = a / b
                return result
            except ZeroDivisionError:
                # Handle division by zero error
                print("Division by zero error")
        else:
            # No arguments provided
            print("Nothing to divide")
