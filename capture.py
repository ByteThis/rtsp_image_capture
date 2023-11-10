import cv2
import os
import time
from datetime import datetime
import argparse
import logging

class ImageCapture:
    def __init__(self, rtsp_url, interval=5, filename_format="im_{timestamp}_{count:04d}.jpg"):
        self.rtsp_url = rtsp_url
        self.interval = interval
        self.filename_format = filename_format
        self.image_count = 0
        self.last_capture_time = time.time()
        self.folder_name = self.create_image_folder()
        self.cap = cv2.VideoCapture(rtsp_url)
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(filename='capture_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

    def create_image_folder(self):
        now = datetime.now()
        folder_name = now.strftime("%Y%m%d-%H%M")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        return folder_name

    def capture_images(self):
        while True:
            ret, frame = self.cap.read()

            if not ret:
                logging.error("Decoding error. Restarting capture...")
                self.cap.release()
                self.cap = cv2.VideoCapture(self.rtsp_url)

            current_time = time.time()
            elapsed_time = current_time - self.last_capture_time

            if elapsed_time >= self.interval:
                self.last_capture_time = current_time
                self.image_count += 1
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                image_name = os.path.join(self.folder_name, self.filename_format.format(timestamp=timestamp, count=self.image_count))
                cv2.imwrite(image_name, frame)
                logging.info(f"Image captured: {image_name}")

    def run(self):
        try:
            self.capture_images()
        except KeyboardInterrupt:
            logging.info("Capture stopped by user.")
        finally:
            self.cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture images from an RTSP feed")
    parser.add_argument("interval", type=int, nargs="?", default=5, help="Capture interval in seconds (default: 5)")
    args = parser.parse_args()

    rtsp_url = "<RTSP_URL>"
    image_capture = ImageCapture(rtsp_url, interval=args.interval)
    image_capture.run()
