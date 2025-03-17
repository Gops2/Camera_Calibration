# Camera Calibration using OpenCV

## Overview
This script performs camera calibration using images of a checkerboard pattern. It estimates the camera matrix and distortion coefficients by detecting checkerboard corners in a set of images.

## Features
- Detects checkerboard corners in calibration images.
- Computes the camera matrix and distortion coefficients.
- Handles cases where checkerboard detection fails.
- Provides output in a readable format.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

## Installation
Ensure you have OpenCV and NumPy installed:

```bash
pip install opencv-python numpy
```

## Usage
1. Place your calibration images in the same directory as the script.
2. Update `image_paths` with the correct filenames.
3. Run the script:

```bash
python camera_calibration.py
```

## Parameters
- **`square_size`**: Size of the checkerboard squares in millimeters (default: `38.1` mm).
- **`pattern_size`**: Number of inner corners in the checkerboard (`(6, 4)`, meaning 6 columns and 4 rows).

## Expected Output
If calibration is successful, the script prints:
- The camera matrix **K**.
- The first two distortion coefficients **k1** and **k2**.

If checkerboard detection fails, an error message is displayed.

## Example Output
```
Camera Matrix, K is:
[[fx  0  cx]
 [ 0 fy  cy]
 [ 0  0   1]]

Distortion Coefficients:
k1: -0.3
k2: 0.2
```

## Notes
- The script assumes that images are named `Q3_pic1.jpg`, `Q3_pic2.jpg`, etc. Update the filenames as necessary.
- The script only prints `k1` and `k2` for brevity but can be modified to display additional distortion coefficients.
- If the checkerboard is not detected in any image, the script will notify the user.
