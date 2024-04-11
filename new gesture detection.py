import cv2
import numpy as np

def detect_gesture(template_path, test_video_path, output_video_path):
    # Read the template image
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)

    # Read the test video
    cap = cv2.VideoCapture(test_video_path)

    # Get template dimensions
    th, tw = template.shape[:2]

    # Define the top-right corner to place the "DETECTED" text
    text_pos = (10, 30)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_color = (0, 255, 0)  # Bright green
    thickness = 2

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'MP4V')
    output_video = cv2.VideoWriter(output_video_path, fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)

        # Define a threshold to consider a match
        threshold = 0.5
        loc = np.where(res >= threshold)

        # Annotate frames where gesture is detected
        for pt in zip(*loc[::-1]):
            cv2.putText(frame, 'DETECTED JUMPING', text_pos, font, font_scale, font_color, thickness)

        # Write the annotated frame to the output video
        output_video.write(frame)

    # Release video capture and writer objects
    cap.release()
    output_video.release()
    cv2.destroyAllWindows()

# Example usage
template_path = 'baby jump.jpg'    # Replace with the path to your template image
test_video_path = 'jumping video.mp4'       # Replace with the path to your test video
output_video_path = 'Output.mp4'   # Specify the output video path
detect_gesture(template_path, test_video_path, output_video_path)