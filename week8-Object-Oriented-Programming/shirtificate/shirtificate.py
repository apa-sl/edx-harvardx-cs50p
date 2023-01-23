# CS50p Problem Set 8: CS50 Shirtificate
# https://cs50.harvard.edu/python/2022/psets/8/shirtificate/
#
# Goal: generate PDF with an image of CS50 t-shirt using fpdf2 module
# Author: Adam Labedzki 2023-01-23

from fpdf import FPDF


class Shirtificate:
    """ Class to create "X took CS50" shirtificate. """
    def __init__(self, name):
        self.name = name
        self.print()


    @classmethod
    def get(cls):
        """ Creates instance of shirtificate. """
        name = input("Full name: ").strip()
        return cls(name)


    def print(self):
        """ Creates PDF with all the details applied. """
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        # set font & add cert title
        pdf.set_font("helvetica", "B", 36)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=30, border=0, align="C", txt="CS50 Shirtificate") #TODO how to use here self.title?
        pdf.ln()

        # add centered t-shirt graphic
        pdf.image(
            "shirtificate.png",
            x = 15,
            y = 297 / 4,
            w = 180,
            alt_text = f"Harvard t-shirt with \"{self.name} took CS50\" inscription",
        )

        # add text on top of the t-shirt grapfic
        pdf.set_font("helvetica", size=28)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(w=0, h=190, border=0, align="C", txt=f"{self.name} took CS50")

        # save PDF to file
        pdf.output("shirtificate.pdf")


    @property
    def name(self):
        """ returns name to be printed on the t-shirt """
        return self._name


    @name.setter
    def name(self, name):
        if not len(str(name)) > 0:
            raise ValueError("Did not provided a proper name")
        self._name = name


def main():
    Shirtificate.get()


if __name__ == "__main__":
    main()