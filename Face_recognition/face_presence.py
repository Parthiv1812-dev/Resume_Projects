import cv2
import time

def main():
    # Try to open default camera (0). If you have multiple cameras, try 1, 2, ...
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Could not access the camera. Try a different index (1, 2) or check permissions.")
        return

    # Load OpenCV's built-in Haar Cascade for frontal faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    if face_cascade.empty():
        print("❌ Could not load Haar Cascade. Check your OpenCV installation.")
        return

    # For FPS calculation (optional)
    prev_time = time.time()
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to read from camera.")
            break

        # Convert to grayscale for the detector
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces (tweak parameters if needed)
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        face_present = len(faces) > 0

        # Draw bounding boxes
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Status text
        status_text = f"Face: {'YES' if face_present else 'NO'}"
        cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0) if face_present else (0, 0, 255), 2)

        # FPS (optional)
        frame_count += 1
        if frame_count >= 10:
            now = time.time()
            fps = frame_count / (now - prev_time)
            prev_time, frame_count = now, 0
            cv2.putText(frame, f"FPS: {fps:.1f}", (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Face Presence Detector - press q to quit", frame)

        # Quit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
