## HSV Conversion

This project aims to alter the hue of given images between an also given interval. This interval is calculated but the difference between "m" and "x" parameters.

It is important to notice that, as we are using cv2 library, the hue is represented with 180 degrees (0 -> 179), with that said, we do need to make the right adaptations to work with this representation.

## How to use it

Upload the imagem on the same height as the main code, after that, update the path within the main page and just:

```python
    python3 main.py
```