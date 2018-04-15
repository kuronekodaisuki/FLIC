from scipy import io
from PIL import Image, ImageDraw

class FLIC:
    def __init__(self, filename):
        mat = io.loadmat(filename)
        self.examples = mat["examples"][0]

    def showKeypoint(self, index):
        example = self.examples[index]
        keypoints = example[2].T
        filename = example[3][0]
        image = Image.open("images/" + filename)
        draw = ImageDraw.Draw(image)

        for x, y in filter(lambda value: 0 <= value[0], keypoints):
            draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 0, 0))

        image.show()

flic = FLIC("examples.mat")
flic.showKeypoint(1)

flic.showKeypoint(10)
