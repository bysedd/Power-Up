from pathlib import Path


class Utils:
    """
    This class contains some utility methods.
    """

    @staticmethod
    def read_file(file: Path) -> list[str]:
        """
        Reads the content of a file and returns it as a list of strings.

        Args:
            file: The file to be read.

        Returns:
            A list of strings, one for each line in the file.
        """
        with open(file, 'r') as f:
            content = f.readlines()
        return [line.strip() for line in content]

    @staticmethod
    def mount_elements(column_names: list[str]) -> dict:
        """
        Mounts a dictionary of elements from a list of column names.

        Args:
            column_names: The names of the columns to generate the elements from.

        Returns:
            A dictionary with the column names as keys and the same column names as values.
        """
        return {column: column for column in column_names}
