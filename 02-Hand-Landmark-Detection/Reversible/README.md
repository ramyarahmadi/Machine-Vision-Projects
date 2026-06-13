##Fix✔🔧
It is enough to evaluate the coordinates of the forearm point with other points.

for z in range(1, 5):
    if landmarks[0].y > landmarks[z].y :
        if landmarks[(4 * z) + 4].y < landmarks[(4 * z) + 2].y:
            fingers[z] = True
    else:
        if landmarks[(4 * z) + 4].y > landmarks[(4 * z) + 2].y:
            fingers[z] = True
