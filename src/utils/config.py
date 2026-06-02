from configparser import ConfigParser
from pathlib import Path
from typing import Dict


def config(file: Path = Path("config.ini"), section: str = "db") -> Dict[str, str]:
    """Get configs from config.ini file

    Parameters
    ----------
    file : Path, optional
        path to the config file, by default Path("config.ini")
    section : str, optional
        section to read from the config file, by default "db"

    Returns
    -------
    Dict[str, str]
        A dictionary containing the configuration values

    Raises
    ------
    FileNotFoundError
        If the config file does not exist
    AttributeError
        If the section is not found in the config file
    """
    parser = ConfigParser()

    if not file.exists():
        raise FileNotFoundError("config file does not exist")
    parser.read(file)

    value = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            value[param[0]] = param[1]
    else:
        raise AttributeError(
            f'Section {section} not found in the {file} file')

    return value


if __name__ == "__main__":
    p_config = config(
        file=Path.cwd() / "config.ini",
        section="db")

    print(p_config)
