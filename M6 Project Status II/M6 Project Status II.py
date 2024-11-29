from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter as tk

class Signs(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Custom Signs")
        self.setResizable(False)
        #Text field to enter the message on the sign
        self.labelMessage = self.addLabel(text = "Enter your message:",row = 0, column=0)
        self.inputMessage = self.addTextField("",row = 0, column = 1)
        #radio buttons to enter the color of the sign
        self.colorGroup = self.addRadiobuttonGroup(row = 1, column = 0)
        self.defaultColor = self.colorGroup.addRadiobutton(text = "Brown")
        self.colorGroup.setSelectedButton(self.defaultColor)
        self.colorGroup.addRadiobutton(text = "Black")
        self.colorGroup.addRadiobutton(text = "White")
        #radio buttons to enter the size of the sign
        self.sizeGroup = self.addRadiobuttonGroup(row =   1, column = 2)
        self.defaultSize = self.sizeGroup.addRadiobutton(text = "12 in X 12 in")
        self.sizeGroup.setSelectedButton(self.defaultSize)
        self.sizeGroup.addRadiobutton(text = "12 in X 18 in")
        #check buttons for custom details
        self.starCB = self.addCheckbutton(text = "Stars", row = 3, column= 0)
        self.flowerCB = self.addCheckbutton(text = "Flowers", row = 3, column = 1)

        #labels with the selected information?
        self.viewOrder = self.addButton(text = "View Order", row = 4, column = 0, command=self.results)
        self.viewAddons = self.addButton(text = "View Add-ons", row = 4, column = 2, command = self.addons)
        self.resetProgram = self.addButton(text = "Clear Order", row = 4, column = 1, command = self.clearProgram)
        self.outputLabel = self.addLabel(text = " ", row = 5, column = 1,sticky = "NSEW")

        #next to enter contact information
        self.submitButton = self.addButton(text = "Submit", row = 10, column = 1, command = self.next)

        self.phoneLabel = self.addLabel(text = "Enter your name: ", row = 6, column = 0)
        self.phoneEntry = self.addTextField(text = "",row = 6, column = 1)
        self.emailLabel = self.addLabel(text = "Enter your email: ", row = 7, column= 0)
        self.emailEntry = self.addTextField(text = "", row = 7, column = 1)
    

    def results(self):
        chosenColor = self.colorGroup.getSelectedButton()["text"]
        choseSize = self.sizeGroup.getSelectedButton()["text"]

        textoutput = "Color: " + chosenColor + "\n" + "Size: " + choseSize

        self.image = None
        self.outputLabel["image"] = self.image
        self.outputLabel = self.addLabel(text = textoutput, row = 5, column = 1, columnspan=2)

    def clearProgram(self):
        self.colorGroup.setSelectedButton(self.defaultColor)
        self.sizeGroup.setSelectedButton(self.defaultSize)
        self.starCB = self.addCheckbutton(text = "Stars", row = 3, column= 0)
        self.flowerCB = self.addCheckbutton(text = "Flowers", row = 3, column = 1)
        self.outputLabel = self.addLabel(text = " ", row = 5, column = 1,sticky = "NSEW")

    def addons(self):
        self.outputLabel = self.addLabel(text = " ", row = 5, column = 1, sticky = "NSEW")
        if self.starCB.isChecked() == True and self.flowerCB.isChecked():
            self.image = PhotoImage(file = "flowers-and-stars.gif")
        elif self.starCB.isChecked() == True:
            self.image = PhotoImage(file = "stars.gif")
        elif self.flowerCB.isChecked() == True:
            self.image = PhotoImage(file = "flowers.gif")
        else:
            self.image = None
        self.outputLabel["image"] = self.image

    def next(self):
        email = self.emailEntry.getText()

        if "@" not in email:
            self.error = self.addLabel(text = "Error, please enter a valid email address", row = 8, column = 0, columnspan = 3)
        else:

            receipt = tk.Toplevel(self)
            receipt.transient(self)
            receipt.title("Receipt")

            title = tk.Label(receipt, text ="The following order has been submitted: ")
            title.grid(row = 0, column = 0, columnspan = 2)

            chosenColor = self.colorGroup.getSelectedButton()["text"]
            chosenSize = self.sizeGroup.getSelectedButton()["text"]

            chosenColorLabel = tk.Label(receipt, text = str("Color: " + chosenColor))
            chosenColorLabel.grid(row = 1, column=1)

            chosenSizeLabel = tk.Label(receipt, text = str("Size: " + chosenSize))
            chosenSizeLabel.grid(row = 2, column = 1)

    
    



def main():
    Signs().mainloop()

if __name__ == "__main__":
    main()