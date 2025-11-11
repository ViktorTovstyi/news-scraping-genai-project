"""
utils.py

General utility functions for logging and debugging in the news scraping project.
"""
def log(message):
    """
    Prints a message to stdout prefixed with [LOG].

    Args:
        message (str): The message string to log.

    Returns:
        None
    """
    print(f"[LOG]: {message}")
