import pandas as pd

class CalculationHistory:
    """
    Class to manage calculation history.
    """
    def __init__(self):
        """
        Initialize the calculation history as an empty DataFrame.
        """
        self.history = pd.DataFrame()

    def add_entry(self, operation, num1, num2, result):
        """
        Add a new entry to the calculation history.

        Args:
            operation (str): The type of operation performed.
            num1 (float): The first number used in the operation.
            num2 (float): The second number used in the operation.
            result (float): The result of the operation.
        """
        new_entry = pd.DataFrame({'Operation': [operation], 'Number1': [num1], 'Number2': [num2], 'Result': [result]})
        if self.history.empty:
            self.history = new_entry
        else:
            self.history = pd.concat([self.history, new_entry], ignore_index=True)

    def display_history(self):
        """
        Display the calculation history.
        """
        print(self.history)

    def save_history(self, filename):
        """
        Save the calculation history to a CSV file.

        Args:
            filename (str): The filename to save the history.
        """
        if not filename.endswith('.csv'):
            filename += '.csv'
        self.history.to_csv(filename, index=False)
        print(f"History saved to {filename}.")

    def clear_history(self):
        """
        Clear the calculation history.
        """
        self.history = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])
        print("History cleared.")

    def delete_entry(self, index):
        """
        Delete an entry from the calculation history by index.

        Args:
            index (int): The index of the entry to delete.
        """
        try:
            self.history.drop(index, inplace=True)
            print("Entry deleted.")
        except KeyError:
            print("Invalid index. Entry does not exist.")
