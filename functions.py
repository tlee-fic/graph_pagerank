# Thomas Lee
# FI Consulting
# Graph PageRank for Predictive Analytics
# functions.py


# Helper Functions supporting Graph PageRank
# Normalize PageRank
def normalize(minVal, maxVal, val):
    normal = (val - minVal) / (maxVal - minVal) if maxVal != minVal else 0.5
    return normal

# PageRank Heat Color
def prGetColor(normScore):
    red = int(normScore * 255)
    green = 0
    blue = int((1 - normScore) * 255)
    return f'rgb({red}, {green}, {blue})'