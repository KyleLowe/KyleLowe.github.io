#Kyle Lowe 4/22/20
#Ticketing Program
from tkinter import *

class TicketInfo:
    
    def __init__(self, match, number, price):
        self.match = match
        self.number = number
        self.price = price

Opening = TicketInfo("Opening Ceremony", 100, 100)
Tables = TicketInfo("Table A and B matches", 100, 50)
Semi1 = TicketInfo("Semi Final 1", 100, 150)
Semi2 = TicketInfo("Semi Fianl 2", 150, 150)
Final = TicketInfo("Finals", 150, 200)
Closing = TicketInfo("Closing Ceremony", 200, 200)

class TicketOrdering:
    
    def CheckTickets(self):
        try:
            TotalTickets = self.OpeningNumber.get() + self.TableNumber.get() + self.Semi1Number.get() + self.Semi2Number.get() + self.FinalNumber.get() + self.ClosingNumber.get()
            if TotalTickets == 0:
                self.TicketNumberError.configure(text = "Error, please order at least 1 ticket")
            elif self.OpeningNumber.get() < 0:
                self.TicketNumberError.configure(text = "Error, you cannot put negative numbers in")
            elif self.TableNumber.get() < 0:
                self.TicketNumberError.configure(text = "Error, you cannot put negative numbers in")
            elif self.Semi1Number.get() < 0:
                self.TicketNumberError.configure(text = "Error, you cannot put negative numbers in")
            elif self.Semi2Number.get() < 0:
                self.TicketNumberError.configure(text = "Error, you cannot put negative numbers in")
            elif self.FinalNumber.get() < 0:
                self.TicketNumberError.configure(text = "Error, you cannot put negative numbers in")
            elif self.ClosingNumber.get() < 0:
                self.TicketNumberError.configure(text = "Error, you cannot put negative numbers in")
            elif self.OpeningNumber.get() > Opening.number:
                self.TicketNumberError.configure(text = "Error, there are not enough tickets for you to buy that amount")                
            elif self.TableNumber.get() > Tables.number:
                self.TicketNumberError.configure(text = "Error, there are not enough tickets for you to buy that amount")
            elif self.Semi1Number.get() > Semi1.number:
                self.TicketNumberError.configure(text = "Error, there are not enough tickets for you to buy that amount")
            elif self.Semi2Number.get() > Semi2.number:
                self.TicketNumberError.configure(text = "Error, there are not enough tickets for you to buy that amount")
            elif self.FinalNumber.get() > Final.number:
                self.TicketNumberError.configure(text = "Error, there are not enough tickets for you to buy that amount")
            elif self.ClosingNumber.get() > Closing.number:
                self.TicketNumberError.configure(text = "Error, there are not enough tickets for you to buy that amount") 
            else:
                self.TotalTicketLabel.configure(text = TotalTickets)
                print (TotalTickets)
                self.PreviewOrder()
            
        except ValueError:
            self.TicketNumberError.configure(text = "Error, please put numbers only")
            
        

    def TicketLists(self):
        self.AddName()
        self.ListOfTickets()

    def AddName(self):
        for name in range(len(self.NameList)):
            order = Label(self.TicketListFrame, bg = "white", fg = "lightblue", text = self.NameList[name], font = ("Times", "12"))
            self.TicketLists.append(order)
            order.grid(row = name + 2, column = 0)
    
    def CheckName(self):
        if self.Name.get() == "":
            self.NameErrorLabel.configure(text = "Please enter a name")
        elif self.Name.get().isalpha() == False:
            self.NameErrorLabel.configure(text = "Please enter letters only")
            self.NameEntry.delete(0, END)
        else:
            self.NameErrorLabel.configure(text = "")
            self.NameList.append(self.Name.get())
            self.PreviewNameLabel.configure(text = self.Name.get())
            self.NameEntry.delete(0, END)
            self.CheckTickets()
            print (self.NameList)


    def PreviewOrder(self):
        self.TicketOrderFrame.grid_remove()
        self.TicketListFrame.grid_remove()
        self.TicketPreviewFrame.grid()

    def Ordering(self):
        self.TicketPreviewFrame.grid_remove()
        self.TicketListFrame.grid_remove()
        self.TicketOrderFrame.grid()
        
    def ListOfTickets(self):
        self.TicketPreviewFrame.grid_remove()
        self.TicketOrderFrame.grid_remove()
        self.TicketListFrame.grid()

   
    def __init__(self, parent):
        #Ticket Order frame
        self.Name = StringVar()
        self.Name.set("")
        self.TicketOrderFrame = Frame(parent, bg = "white")
        self.TicketOrderFrame.grid(row = 0, column = 0)
        self.TitleLabel = Label(self.TicketOrderFrame, bg = "white", fg= "lightblue", text = "ICC T20 World Cup Ticket Purchases", font = ("Times", "14", "bold"))
        self.TitleLabel.grid(columnspan = 4)
        self.NameLabel = Label(self.TicketOrderFrame, bg = "white", fg= "lightblue", text = "Please Enter name", font = ("Times", "12"))
        self.NameLabel.grid(row = 1, column = 0)
        self.NameEntry = Entry(self.TicketOrderFrame, bg = "white", fg= "black", font = ("Times", "12"), textvariable = self.Name)
        self.NameEntry.grid(row = 1, column = 3)
        self.MatchesLabel = Label(self.TicketOrderFrame, bg = "white", fg= "lightblue", text = "Matches", font = ("Times", "12"))
        self.MatchesLabel.grid(row = 3, column = 0)
        self.NoOfTicketsLabel = Label(self.TicketOrderFrame, bg = "white", fg= "lightblue", text = "Number of tickets avaliable", font = ("Times", "12"))
        self.NoOfTicketsLabel.grid(row = 3, column = 1)
        self.TicketPricesLabel = Label(self.TicketOrderFrame, bg = "white", fg= "lightblue", text = "Price of tickets", font = ("Times", "12"))
        self.TicketPricesLabel.grid(row = 3, column = 2)
        self.PurchaseTicketLabel = Label(self.TicketOrderFrame, bg = "white", fg= "lightblue", text = "Purchase Tickets", font = ("Times", "12"))
        self.PurchaseTicketLabel.grid(row = 3, column = 3)
        self.NameErrorLabel = Label(self.TicketOrderFrame, bg = "white", fg = "black", text = "", font = ("Times", "12"))
        self.NameErrorLabel.grid(row = 2, column = 3)

        
        #Tickets
        self.TicketsMatch = [Opening, Tables, Semi1, Semi2, Final, Closing]
        self.TicketsMatchName = []
        self.TicketsPrices = []
        self.TicketsNumberOfTickets = []
        
        for ticket in range(len(self.TicketsMatch)):
            matches = Label(self.TicketOrderFrame, text = self.TicketsMatch[ticket].match, bg = "white", fg= "lightblue")
            self.TicketsMatchName.append(ticket)
            matches.grid(row = ticket + 4, column = 0)
            number = Label(self.TicketOrderFrame, text = self.TicketsMatch[ticket].number, bg = "white", fg= "lightblue")
            self.TicketsNumberOfTickets.append(ticket)
            number.grid(row = ticket + 4, column = 1)
            price = Label(self.TicketOrderFrame, text = "$" + str(self.TicketsMatch[ticket].price), bg = "white", fg= "lightblue")
            self.TicketsPrices.append(ticket)
            price.grid(row = ticket + 4, column = 2)
        self.OpeningNumber = IntVar()
        self.OpeningEntry = Entry(self.TicketOrderFrame, bg = "white", fg = "black", textvariable = self.OpeningNumber)
        self.OpeningEntry.grid(row = 4, column = 3)
        self.TableNumber = IntVar()
        self.TableEntry = Entry(self.TicketOrderFrame, bg = "white", fg = "black", textvariable = self.TableNumber)
        self.TableEntry.grid(row = 5, column = 3)
        self.Semi1Number = IntVar()
        self.Semi1Entry = Entry(self.TicketOrderFrame, bg = "white", fg = "black", textvariable = self.Semi1Number)
        self.Semi1Entry.grid(row = 6, column = 3)
        self.Semi2Number = IntVar()
        self.Semi2Entry = Entry(self.TicketOrderFrame, bg = "white", fg = "black", textvariable = self.Semi2Number)
        self.Semi2Entry.grid(row = 7, column = 3)
        self.FinalNumber = IntVar()
        self.FinalEntry = Entry(self.TicketOrderFrame, bg = "white", fg = "black", textvariable = self.FinalNumber)
        self.FinalEntry.grid(row = 8, column = 3)
        self.ClosingNumber = IntVar()
        self.ClosingEntry = Entry(self.TicketOrderFrame, bg = "white", fg = "black", textvariable = self.ClosingNumber)
        self.ClosingEntry.grid(row = 9, column = 3)
        self.TicketNumberError = Label(self.TicketOrderFrame, bg = "white", fg = "black", text = "")
        self.TicketNumberError.grid(row = 10, column = 3)
        self.ConfirmButton = Button(self.TicketOrderFrame, bg = "white", fg = "black", command = self.CheckName, text = "Preview Order")
        self.ConfirmButton.grid(row = 11, column = 3)

        #Ticket Preview Frame
        self.TicketPreviewFrame = Frame(parent, bg = "white")
        self.TitleLabel = Label(self.TicketPreviewFrame, bg = "white", fg= "lightblue", text = "ICC T20 World Cup Ticket Purchases Preview", font = ("Times", "14", "bold"))
        self.TitleLabel.grid(columnspan = 4)
        self.TicketNameLabel = Label(self.TicketPreviewFrame, bg = "white", fg= "lightblue", text = "Ticket Name", font = ("Times", "12"))
        self.TicketNameLabel.grid(row = 1, column = 0)
        self.NumberOfTicketLabel = Label(self.TicketPreviewFrame, bg = "white", fg= "lightblue", text = "Number of Tickets Purchased", font = ("Times", "12"))
        self.NumberOfTicketLabel.grid(row = 1, column = 1)
        self.TicketPriceLabel = Label(self.TicketPreviewFrame, bg = "white", fg= "lightblue", text = "Ticket Price", font = ("Times", "12"))
        self.TicketPriceLabel.grid(row = 1, column = 2)
        self.PreviewNameLabel = Label(self.TicketPreviewFrame, bg = "white", fg = "lightblue", text = "", font = ("Times", "12"))
        self.PreviewNameLabel.grid(row = 5, column = 0)
        self.TotalTicketsLabel = Label(self.TicketPreviewFrame, bg = "white", fg = "lightblue", text = "", font = ("Times", "12"))
        self.TotalTicketsLabel.grid(row = 5, column = 1)
        self.TotalTicketPrice = Label(self.TicketPreviewFrame, bg = "white", fg = "lightblue", text = "", font = ("Times", "12"))
        self.TotalTicketPrice.grid(row = 5, column = 2)
        self.OrderButton = Button(self.TicketPreviewFrame, bg = "white", fg = "black", command = self.Ordering, text = "Back to Ordering")
        self.OrderButton.grid(row = 6, column = 0)
        self.ListButton = Button(self.TicketPreviewFrame, bg = "white", fg = "black", command = self.TicketLists, text = "Confirm Order")
        self.ListButton.grid(row = 6, column = 2)



        #Ticket List of Ordered Tickets
        self.NameList = []
        self.TotalTicketList = []
        self.TicketLists = []
        self.TicketListFrame = Frame(parent, bg = "white")
        self.TitleLabel = Label(self.TicketListFrame, bg = "white", fg= "lightblue", text = "ICC T20 World Cup Ticket Purchases List", font = ("Times", "14", "bold"))
        self.TitleLabel.grid(columnspan = 4)
        self.NameListLabel = Label(self.TicketListFrame, bg = "white", fg= "lightblue", text = "Name List", font = ("Times", "14", "bold"))
        self.NameListLabel.grid(row = 1, column = 0)
        self.TicketsListLabel = Label(self.TicketListFrame, bg = "white", fg= "lightblue", text = "Tickets Purchased", font = ("Times", "14", "bold"))
        self.TicketsListLabel.grid(row = 1, column = 1)
        self.NameLabel = Label(self.TicketListFrame, bg = "white", fg= "lightblue", text = "Total Price", font = ("Times", "14", "bold"))
        self.NameLabel.grid(row = 1, column = 2)
        self.OrderButton = Button(self.TicketListFrame, bg = "white", fg = "black", command = self.Ordering, text = "Back to Ordering")
        self.OrderButton.grid(row = 6, column = 0)

        





if __name__ == "__main__":
    root = Tk()
    frames = TicketOrdering(root)
    root.title("ICC T20 World Cup Tickets")
    root.mainloop()
