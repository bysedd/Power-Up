from pathlib import Path


class Utils:

    @staticmethod
    def read_file(file: Path) -> list[str]:
        with open(file, 'r') as f:
            content = f.readlines()
        # Remover o '\n' do final de cada linha
        return [line.strip() for line in content]

    @staticmethod
    def mount_elements(column_names: list[str]) -> dict:
        return dict((column, column) for column in column_names)
