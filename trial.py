import tkinter as tk
import cv2
from PIL import Image, ImageTk



class VideoCapture:
    def __init__(self, window):
        self.window = window
        self.cap = cv2.VideoCapture(0)
        self.canvas = tk.Canvas(window, width=self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()

    def update(self):
        ret, frame = self.cap.read()
        if ret:
            self.photo = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = cv2.resize(self.photo, (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.photo))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(15, self.update)

    def close(self):
        self.cap.release()

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Video Capture")

    video_capture = VideoCapture(window)

    window.protocol("WM_DELETE_WINDOW", video_capture.close)

    video_capture.update()
    window.mainloop()
