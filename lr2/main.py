import cv2 as cv
from tkinter import ttk, Tk
from PIL import ImageTk, Image


def return_function(img):
    img = Image.fromarray(img)
    img = img.resize((300, 300))
    return ImageTk.PhotoImage(img)


class MainSolution:
    def __init__(self):
        self.image = cv.imread("coins.jpg")

    def apply_filters(self):
        def create_label_and_place(text, x, y):
            lbl_text = ttk.Label(text=text)
            lbl_text.place(x=x, y=y)

        def create_image_label_and_place(img, x, y, width, height):
            lbl = ttk.Label(image=img)
            lbl.image = img
            lbl.place(x=x, y=y, width=width, height=height)

        create_label_and_place("Изначальное изображение", 90, 10)
        create_label_and_place("Глобальная пороговая обработка", 400, 10)
        create_label_and_place("Адаптивная пороговая обработка", 90, 360)
        create_label_and_place("Сглаживающий низкочастотный фильтр", 400, 360)

        img1 = self.to_gray_filter()
        create_image_label_and_place(img1, 30, 40, 300, 300)

        img2 = self.global_threshold()
        create_image_label_and_place(img2, 370, 40, 300, 300)

        img3 = self.adaptive_threshold()
        create_image_label_and_place(img3, 30, 390, 300, 300)

        img4 = self.low_pass_filter()
        create_image_label_and_place(img4, 370, 390, 300, 300)

    def to_gray_filter(self):
        self.image = cv.cvtColor(cv.pyrMeanShiftFiltering(
            self.image, 15, 50), cv.COLOR_BGR2GRAY)
        return return_function(self.image)

    def global_threshold(self):
        ret, thresh1 = cv.threshold(self.image, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        return return_function(thresh1)

    def adaptive_threshold(self):
        thresh2 = cv.adaptiveThreshold(self.image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
        return return_function(thresh2)

    def low_pass_filter(self):
        img = cv.GaussianBlur(self.image, (11, 11), 0)
        return return_function(img)


if __name__ == "__main__":
    root = Tk()
    ms = MainSolution()
    root.geometry(f"700x700")
    ms.apply_filters()
    root.mainloop()
