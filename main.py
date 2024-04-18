import os
import webbrowser

from fpdf import FPDF


class Bill:
    """
    object that contains bill amount, period
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    contains flatmate details
    """

    def __init__(self, name, days_in_flat):
        self.name = name
        self.days_in_flat = days_in_flat

    def pays(self, bill, flatmate2):
        weight = self.days_in_flat / (self.days_in_flat + flatmate2.days_in_flat)
        to_pay = bill.amount * weight
        return to_pay


class PdfGenerate:
    """
    generates bill in pdf format
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.image("assets/homrece.png", w=30, h=30)

        # add text to pdf (Period, label)_
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(f"assets/{self.filename}")
        webbrowser.open('file://' + os.path.realpath(f"assets/{self.filename}"))


amount = float(input("Hey, please enter the bill amount "))
period = input("enter the period, e.g. December 2022 ")

name1 = input("What is your name? ")
days_in_flat1 = int(input("How many days did you stay in the Flat "))

name2 = input("What is the name of the other flatmate? ")
days_in_flat2 = int(input(f"How many days did {name2} stay in the Flat "))

bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_flat1)
flatmate2 = Flatmate(name2, days_in_flat2)

# print("John Pays: ", john.pays(bill, mary))
# print("Mary Pays: ", mary.pays(bill, john))

pdf_report = PdfGenerate("bill.pdf")
pdf_report.generate(flatmate1, flatmate2, bill)
