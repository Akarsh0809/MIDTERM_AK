import pandas as pd

class CalculationHistory:
    """
    Class to manage calculation history.
    """

    def __init__(self):
        """
        Initialize the calculation history as an empty DataFrame.
        """
        self.history_df = pd.DataFrame()

    def add_entry(self, operation, number1, number2, result):
        """
        Add a new entry to the calculation history.

        Args:
            operation (str): The type of operation performed.
            number1 (float): The first number used in the operation.
            number2 (float): The second number used in the operation.
            result (float): The result of the operation.
        """
        new_entry = pd.DataFrame({'Operation': [operation], 'Number1': [number1], 'Number2': [number2], 'Result': [result]})
        if self.history_df.empty:
            self.history_df = new_entry
        else:
            self.history_df = pd.concat([self.history_df, new_entry], ignore_index=True)

    def display_history(self):
        """
        Display the calculation history.
        """
        print(self.history_df)

    def save_history(self, filename):
        """
        Save the calculation history to a CSV file.

        Args:
            filename (str): The filename to save the history.
        """
        if not filename.endswith('.csv'):
            filename += '.csv'
        self.history_df.to_csv(filename, index=False)
        print(f"History saved to {filename}.")

    def clear_history(self):
        """
        Clear the calculation history.
        """
        self.history_df = pd.DataFrame(columns=['Operation', 'Number1', 'Number2', 'Result'])
        print("History cleared.")

    def delete_entry(self, index):
        """
        Delete an entry from the calculation history by index.

        Args:
            index (int): The index of the entry to delete.
        """
        try:
            self.history_df.drop(index, inplace=True)
            print("Entry deleted.")
        except KeyError:
            print("Invalid index. Entry does not exist.")
