# RTSP Image Capture

**A versatile Python tool for capturing images from RTSP streams with customizable intervals. Ideal for surveillance cameras, time-lapse photography and 3D printer cameras**

## Features

- Captures images from an RTSP feed at specified intervals.
- Customizable capture interval (default: 5 seconds).
- Configurable filename format for captured images.
- Handles decoding errors by restarting the capture.
- Logs capture activities to a file (`capture_log.txt`).

## Prerequisites

- Python 3.x
- OpenCV (`cv2` library)

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/RTSP-Image-Capture.git
    ```

2. **Install the required dependencies:**

    ```bash
    pip install opencv-python
    ```

3. **Run the script with the desired RTSP URL:**

    ```bash
    python capture_images.py [interval]
    ```

    Example:

    ```bash
    python capture_images.py rtsp://user:pass@your-camera-url/stream 10
    ```
    - `[interval]`: Optional argument for the capture interval in seconds (default: 5).

4. **Stop the capture using `Ctrl+C`.**

## Configuration

- Adjust the default capture interval and filename format by modifying the script's arguments and parameters.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with Python and OpenCV.
