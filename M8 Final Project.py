"""

Author:  Emma Foust
Date written: 12/8/24
Assignment:   Module8 Final Project
Short Desc:   This program creates a GUI for submitting an order for a custom wooden sign


"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter as tk
from tkinter.font import Font

class Signs(EasyFrame):
    def __init__(self):
        """Creates the main window for the 'Custom Signs' GUI, which includes text entry,
        multiple choice buttons, and clear and submit buttons."""
        EasyFrame.__init__(self, title = "Custom Signs")
        self.setResizable(False)
        #Text field to enter the message on the sign
        self.labelMessage = self.addLabel(text = "Enter your message:",row = 0, column=0)
        self.inputMessage = self.addTextField("",row = 0, column = 1)
        #radio buttons to enter the color of the sign
        self.radioLabel = self.addLabel(text = "Choose the sign's color and size:", row = 1, column = 0, columnspan= 2)

        self.colorGroup = self.addRadiobuttonGroup(row = 2, column = 0)
        self.defaultColor = self.colorGroup.addRadiobutton(text = "Brown")
        self.colorGroup.setSelectedButton(self.defaultColor)
        self.colorGroup.addRadiobutton(text = "Black")
        self.colorGroup.addRadiobutton(text = "White")
        #radio buttons to enter the size of the sign
        self.sizeGroup = self.addRadiobuttonGroup(row =   2, column = 1)
        self.defaultSize = self.sizeGroup.addRadiobutton(text = "12 in X 12 in")
        self.sizeGroup.setSelectedButton(self.defaultSize)
        self.sizeGroup.addRadiobutton(text = "12 in X 18 in")
        #check buttons for custom details
        self.checkLabel = self.addLabel(text = "Choose add-ons: (Optional)", row = 3, column = 0, columnspan= 2)

        self.starCB = self.addCheckbutton(text = "Stars", row = 4, column= 0)
        self.flowerCB = self.addCheckbutton(text = "Flowers", row = 4, column = 1)

        #buttons for viewing and clearing the selections
        buttonPanel = self.addPanel(row = 5, column = 0, columnspan= 2)

        buttonPanel.addButton(text = "View Order", row = 0, column = 0, command=self.results) #button to display the selected options
        buttonPanel.addButton(text = "View Add-ons", row = 0, column = 2, command = self.addons) #button to view images of the add-ons
        buttonPanel.addButton(text = "Clear Order", row = 0, column = 1, command = self.clearProgram) #button to clear the selections / inputs
        
        self.outputLabel = self.addLabel(text = " ", row = 6, column = 0,columnspan= 2,sticky = "NSEW") #label to contain the order details

        #enter contact information
        self.nameLabel = self.addLabel(text = "Enter your name: ", row = 8, column = 0)
        self.nameEntry = self.addTextField(text = "",row = 8, column = 1)
        self.emailLabel = self.addLabel(text = "Enter your email: ", row = 9, column= 0)
        self.emailEntry = self.addTextField(text = "", row = 9, column = 1)
        self.error = self.addLabel(text="", row = 10, column=0, columnspan=2) #label to contain any error messages

        #Submit order to view reciept
        self.submitButton = self.addButton(text = "Submit", row = 11, column = 0, command = self.next)
        
        #Close program
        self.quitButton = self.addButton(text = "Quit", row = 11, column = 1, command= self.quit)
    

    def results(self):
        """Displays the Order"""
        chosenColor = self.colorGroup.getSelectedButton()["text"] #the color the user selected
        chosenSize = self.sizeGroup.getSelectedButton()["text"] #the sign size the user selected
        chosenAdd1 = self.starCB.isChecked() #boolean value for the state of the add-on check box
        chosenAdd2 = self.flowerCB.isChecked() #boolean value for the state of the add-on check box

        #string containing the order details
        textoutput = "Color: " + chosenColor + "\n" + "Size: " + chosenSize
        #if one or both of the add-on check boxes are selected, the corresponding text is
        #added to the output string
        if chosenAdd1 == True and chosenAdd2 == True:
            textoutput = textoutput + "\n" + "Add-ons: Star and Flower Pattern"
        elif chosenAdd1 == True:
            textoutput = textoutput + "\n" + "Add-ons: Star Pattern"
        elif chosenAdd2 == True:
            textoutput = textoutput + "\n" + "Add-ons: Flower Pattern"

        #image of any add-ons must be removed in order to display the order detail text
        self.image = None
        self.outputLabel["image"] = self.image
        self.caption = self.addLabel(" ", row = 7, column = 0, columnspan= 2,sticky = "NSEW")
        #the order details are displayed
        self.outputLabel = self.addLabel(text = textoutput, row = 6, column = 0, columnspan=2,sticky = "NSEW")

    def clearProgram(self):
        """Clears the user's checkbox selections and returns the radio button selections to their defaults."""
        self.colorGroup.setSelectedButton(self.defaultColor)
        self.sizeGroup.setSelectedButton(self.defaultSize)
        self.starCB = self.addCheckbutton(text = "Stars", row = 4, column= 0)
        self.flowerCB = self.addCheckbutton(text = "Flowers", row = 4, column = 1)
        self.outputLabel = self.addLabel(text = " ", row = 6, column = 0, columnspan= 2, sticky = "NSEW")
        self.caption = self.addLabel(" ", row = 7, column = 0, columnspan= 2,sticky = "NSEW")
        self.error["text"] = ""
        self.inputMessage.setText("")

    def addons(self):
        """Displays an image of the selected 'add on'."""
        self.outputLabel = self.addLabel(text = " ", row = 6, column = 0, columnspan= 2, sticky = "NSEW")
        if self.starCB.isChecked() == True and self.flowerCB.isChecked():
            self.image = PhotoImage(file = "flowers-and-stars.gif")
            #caption for the image, containing different text depending on which add-on is being displayed.
            self.caption = self.addLabel("Flower and Star Pattern", row = 7, column = 0, columnspan= 2,sticky = "NSEW")
        elif self.starCB.isChecked() == True:
            self.image = PhotoImage(file = "stars.gif")
            self.caption = self.addLabel("Star Pattern", row = 7, column = 0, columnspan= 2,sticky = "NSEW")
        elif self.flowerCB.isChecked() == True:
            self.image = PhotoImage(file = "flowers.gif")
            self.caption = self.addLabel("Flower Pattern", row = 7, column = 0, columnspan= 2,sticky = "NSEW")
        else:
            self.image = None
            self.caption = self.addLabel(" ", row = 7, column = 0, columnspan= 2,sticky = "NSEW")
        self.outputLabel["image"] = self.image
        #font style and size for the image caption
        self.caption["font"] = Font(family = "Ariel", weight = "bold", size = 12) 

    def next(self):
        """Checks if the email contains an '@' symbol, to make sure it is a real address.
        Checks to see if there is a entry in the 'name entry' text field.
        Checks if the message is less than 100 characters
        If all of these entries are valid, a new window is created showing the reciept."""
        email = self.emailEntry.getText() #user entry in the 'email' text field
        name = self.nameEntry.getText() #user entry in the 'name' text field
        message = self.inputMessage.getText() #user entry in the 'message' text field
        self.error["text"] = "" #clearing any error message that might already be present

        #Check if there is a valid entry in each text field. 
        if len(message) > 100:
            self.error = self.addLabel(text = "Error, please enter a message below 100 characters", row = 10, column = 0, columnspan=2)     
        elif len(name) == 0:
            self.error = self.addLabel(text = "Error, please enter your name.", row = 10, column= 0, columnspan= 2)
        elif "@" not in email:
            self.error = self.addLabel(text = "Error, please enter a valid email address", row = 10, column = 0, columnspan = 2)
        else:
            #creating the new 'receipt' window
            receipt = tk.Toplevel(self)
            receipt.transient(self)
            receipt.title("Receipt")

            #title for the receipt
            title = tk.Label(receipt, text ="The following order has been submitted: ")
            title.grid(row = 0, column = 0, columnspan = 3)

            #user selected options for color and size
            chosenColor = self.colorGroup.getSelectedButton()["text"]
            chosenSize = self.sizeGroup.getSelectedButton()["text"]

            #checking the state of the add-on check boxes
            choseAdd1 = self.starCB.isChecked()
            choseAdd2 = self.flowerCB.isChecked()

            #strings containing the user selections for color and size
            chosenColorLabel = tk.Label(receipt, text = str("Color: " + chosenColor))
            chosenColorLabel.grid(row = 1, column=1)

            chosenSizeLabel = tk.Label(receipt, text = str("Size: " + chosenSize))
            chosenSizeLabel.grid(row = 2, column = 1)

            #if one or both of the add-on boxes were checked, that information is added to
            #the receipt window.
            if choseAdd1 == True and choseAdd2 == True:
                chosenPatternLabel = tk.Label(receipt, text = str("Add ons: Star and Flower Pattern"))
                chosenPatternLabel.grid(row = 3, column = 1)
            elif choseAdd1 == True:
                chosenPatternLabel = tk.Label(receipt, text = str("Add ons: Star"))
                chosenPatternLabel.grid(row = 3, column = 1)
            elif choseAdd2 == True:
                chosenPatternLabel = tk.Label(receipt, text = str("Add ons: Flower Pattern"))
                chosenPatternLabel.grid(row = 3, column = 1)
def quit(Signs):
    """Closes the program"""
    Signs.destroy()

def main():
    Signs().mainloop()

if __name__ == "__main__":
    main()