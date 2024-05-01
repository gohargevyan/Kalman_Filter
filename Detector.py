import pyautogui
import numpy as np

def detect(frame, debugMode):
    """
    Detect function to return cursor position.
    
    :param frame: Input frame (not used in cursor tracking)
    :param debugMode: Debug mode flag (not used in cursor tracking)
    :return: List containing numpy array representing cursor position
    """
    # Get cursor position
    cursor_x, cursor_y = pyautogui.position()

    # Return cursor position as a list of numpy arrays
    return [np.array([[cursor_x], [cursor_y]])]
