## HSV Conversion

This project aims to alter the hue of given images between an also given interval. This interval is calculated by the difference between "m" and "x" parameters.

It is important to notice that, as we are using cv2 library, the hue is represented with 180 degrees (0 -> 179), with that said, we do need to make the right adaptations to work with this representation.

## How to use it

Upload the image on the "files" folder, after that, run the program as usual:

```python
    python3 main.py
```

There will be a menu plotted on the terminal, choose [1] to list all images available, choose [2] to alter the hue of any image inside the files folder and choose [3] to quit.

## Dependencies
1. matplotlib
2. cv2

To install them, make sure you have pip or pip3 installed and run: 

```bash
    python -m pip install -U matplotlib
    pip install opencv-python
```