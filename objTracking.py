import cv2
import pyautogui  # Import the pyautogui library
from KalmanFilter import KalmanFilter
import numpy as np

def main():
    # Create KalmanFilter object KF
    # KalmanFilter(dt, u_x, u_y, std_acc, x_std_meas, y_std_meas)
    KF = KalmanFilter(0.1, 1, 1, 1, 0.1, 0.1)
    size = (1080, 1920)
    title = 'Filter'
    debugMode = 1
    cv2.namedWindow(title, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(title,cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
        
    while True:
        frame = np.zeros(size)
        # print(frame.shape)
        # Get cursor position
        cursor_x, cursor_y = pyautogui.position()

        # Predict
        X = KF.predict()

        # Update
        (x1, y1) = KF.update((cursor_x, cursor_y))
        # print([0][-1])
        X = X.tolist()[0]
        # print(X)
        # if len(X[0]) == 1: continue

        # Display cursor position with Kalman filter estimation
        # print("Cursor Position: ({}, {}) Estimated Position: ({}, {})".format(cursor_x, cursor_y, x, y))
        # print((max(0, int(x[0][0]-5)), max(0, int(y[0][0]-5))), (max(0, int(x[0][0]+5)), max(0, int(y[0][0]+5))))
        # input()
        try:
            cv2.rectangle(frame, (max(0, int(X[0]-30)), max(0, int(X[-1]-30))), (max(0, int(X[0]+30)), max(0, int(X[-1]+30))), (255, 0, 0), 3)
            cv2.imshow(title, frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        except:
            continue
        


if __name__ == "__main__":
    # Execute main
    main()


