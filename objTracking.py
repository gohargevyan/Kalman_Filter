import cv2
import pyautogui  # Import the pyautogui library
from KalmanFilter import KalmanFilter

def main():
    # Create KalmanFilter object KF
    # KalmanFilter(dt, u_x, u_y, std_acc, x_std_meas, y_std_meas)
    KF = KalmanFilter(0.1, 1, 1, 1, 0.1, 0.1)

    debugMode = 1

    while True:
        # Get cursor position
        cursor_x, cursor_y = pyautogui.position()

        # Predict
        (x, y) = KF.predict()

        # Update
        (x1, y1) = KF.update((cursor_x, cursor_y))

        # Display cursor position with Kalman filter estimation
        print("Cursor Position: ({}, {}) Estimated Position: ({}, {})".format(cursor_x, cursor_y, x1, y1))

if __name__ == "__main__":
    # Execute main
    main()


