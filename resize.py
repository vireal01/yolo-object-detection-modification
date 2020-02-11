def resize(img_height, img_weight, screen_weight, screen_height):
    multipliers = []
    if img_weight > screen_weight:
        multipliers.append(round(float((screen_weight -100)/ img_weight), 2))
    if img_height > screen_height:
        multipliers.append(round(float((screen_height -100)/ img_height), 2))
    else:
        multipliers.append(1)
    multiplier = min(multipliers)
    return multiplier


