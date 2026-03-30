# Sample source code


def add(a: int, b: int) -> int:
    """
    Add two numbers together

    Parameters
    ----------
    a : int
        The first number
    b : int
        The second number

    Returns
    -------
    int
        The sum of the two numbers
    """
    return a + b

def explane():
    """
    This is a sample function to demonstrate the use of docstrings and logging.
    """
    from utils.logger import setup_logger
    logger = setup_logger("sample")
    logger.info("This is an info message from the sample function.")
    logger.warning("This is a warning message from the sample function.")
    logger.error("This is an error message from the sample function.")
    from utils.config import load_config
    config = load_config(".config/general.json")
    logger.info(f"Loaded config: {config}")

if __name__ == "__main__":
    explane()
