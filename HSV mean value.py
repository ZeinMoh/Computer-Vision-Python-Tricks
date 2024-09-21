import cv2
import numpy as np

def get_mean_hsv(roi):
    # Convert the ROI to HSV
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # Calculate the mean HSV values
    mean_hue = np.mean(hsv_roi[:, :, 0])
    mean_saturation = np.mean(hsv_roi[:, :, 1])
    mean_value = np.mean(hsv_roi[:, :, 2])

    return mean_hue, mean_saturation, mean_value

def main():
    # Capture video from the default camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        return

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            break

        # Display the frame
        cv2.imshow("Video Frame", frame)

        # Wait for a key press and check if it's 'c' (for capture)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            # Select ROI
            roi = cv2.selectROI("Video Frame", frame, fromCenter=False, showCrosshair=True)
            if roi[2] > 0 and roi[3] > 0:
                # Crop the ROI from the frame
                roi_cropped = frame[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

                # Get the mean HSV values of the ROI
                mean_hue, mean_saturation, mean_value = get_mean_hsv(roi_cropped)

                # Display the mean HSV values
                print(f"Mean HSV values: H = {mean_hue}, S = {mean_saturation}, V = {mean_value}")

        # Break the loop if 'q' is pressed
        elif key == ord('q'):
            break

    # Release the video capture object and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
