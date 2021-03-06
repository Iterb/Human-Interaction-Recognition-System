import cv2
import numpy as np

CLASS_DICT = {
    0: "punch",
    1: "kicking",
    2: "pushing",
    3: "pat on back",
    4: "point finger",
    5: "hugging",
    6: "giving an object",
    7: "touch pocket",
    8: "shaking hands",
    9: "walking towards",
    10: "walking apart",
}


def put_interactions_on_video(
    video_path: str,
    interactions: np.array,
    window_duration: int,
    window_offset: int,
    output_path: str,
):
    cap = cv2.VideoCapture(video_path)
    out = cv2.VideoWriter(
        "out2.avi",
        cv2.VideoWriter_fourcc(*"XVID"),
        cap.get(cv2.CAP_PROP_FPS),
        (int(cap.get(3)), int(cap.get(4))),
    )
    fps = cap.get(cv2.CAP_PROP_FPS)
    current_frame_number = -1
    predicted_classes = np.argmax(interactions, axis=1)

    width = int(cap.get(3))  # float `width`
    height = int(cap.get(4))  # float `height`
    while True:
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
        # Capture frame-by-frame
        current_frame_number += 1
        ret, frame = cap.read()
        current_second = np.floor(current_frame_number / fps)
        current_index = window_offset * current_second
        print(current_index)
        try:
            predicted_class = predicted_classes[int(current_index)]
            cv2.rectangle(
                frame,
                (0, int(height - height * 0.1)),
                (width, height),
                (255, 255, 255),
                -1,
            )
            cv2.putText(
                frame,
                f"{CLASS_DICT[predicted_class]}",
                (15, height - 5),
                0,
                5e-3 * int(height * 0.6),
                (0, 0, 0),
                1,
            )
            # cv2.imshow("Out", frame)
            out.write(frame)
        except:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()
