import tkinter as tk
from tkinter import messagebox, Tk, Label, Entry, Button, END

class Transaction():
    def __init__(self, id_customer):
        self.id_customer = id_customer
        self.nama_item = dict()
    
    def add_item(self, nama_item, jumlah_item, harga):
        self.nama_item[nama_item] = [jumlah_item, harga]
    
    def update_name_item(self, nama_item, new_name):
        if nama_item in self.nama_item:
            self.nama_item[new_name] = self.nama_item.pop(nama_item)
    
    def update_jumlah_item(self, nama_item, new_jumlah):
        if nama_item in self.nama_item:
            self.nama_item[nama_item][0] = new_jumlah
    
    def update_harga(self, nama_item, new_harga):
        if nama_item in self.nama_item:
            self.nama_item[nama_item][1] = new_harga
    
    def update_item(self, nama_item):
        for key in self.nama_item:
            if key == nama_item:
                return key
        return None
    
    def delete_item(self, nama_item):
        if nama_item in self.nama_item:
            del self.nama_item[nama_item]
            print(f"Item {nama_item} berhasil dihapus.")
        else:
            print(f"Tidak ditemukan item dengan nama {nama_item}.")
         
    def total_price(self):
        total = 0
        for key, value in self.nama_item.items():
            total += value[0] * value[1]

        if total > 500000:
            total *= 0.9
            diskon = "10%"
        elif total > 300000:
            total *= 0.92
            diskon = "8%"
        elif total > 200000:
            total *= 0.95
            diskon = "5%"
        else:
            diskon = "0%"

        return total, diskon
    
    def print_receipt(self):
        total_harga, diskon = self.total_price()
        total_harga_setelah_diskon = total_harga
        if diskon != "0%":
            total_harga_setelah_diskon = total_harga - (total_harga * float(diskon.strip('%')) / 100)

        print(f"===== Struk Belanjaan =====")
        print(f"ID Customer: {self.id_customer}")
        print(f"{'Item':<10} {'Jumlah':<10} {'Harga':<10}")
        for item in self.nama_item:
            print(f"{item:<10} {self.nama_item[item][0]:<10} {self.nama_item[item][1]:<10}")
        print(f"{'Total Harga':<20} {total_harga:<10}")
        print(f"{'Diskon':<20} {diskon}")
        print(f"{'Total Harga Setelah Diskon':<20} {total_harga_setelah_diskon:<10}")
        print(f"==========================")


class TransactionGUI():
    def __init__(self, master):
        self.master = master
        master.title("Transaction GUI")
        master.geometry("500x400")
        self.master.resizable(False, False)

        # Create customer id label and entry
        self.id_label = tk.Label(master, text="Customer ID:")
        self.id_label.place(x=50, y=10)
        self.id_entry = tk.Entry(master)
        self.id_entry.place(x=200, y=10)

        # create and position the widgets
        self.label1 = tk.Label(master, text="Item Name:")
        self.label1.place(x=50, y=50)
        self.entry1 = tk.Entry(master)
        self.entry1.place(x=200, y=50)
        
        self.label5 = tk.Label(master, text="Item Quantity:")
        self.label5.place(x=50, y=75)
        self.entry5 = tk.Entry(master)
        self.entry5.place(x=200, y=75)

        self.label2 = tk.Label(master, text="Item Price:")
        self.label2.place(x=50, y=100)
        self.entry2 = tk.Entry(master)
        self.entry2.place(x=200, y=100)

        self.button1 = tk.Button(master, text="Add Item", command=self.add_item)
        self.button1.place(x=200, y=150)
        
        self.label3 = tk.Label(master, text="Total Price:")
        self.label3.place(x=50, y=200)
        self.total_price = tk.StringVar()
        self.label4 = tk.Label(master, textvariable=self.print_receipt)
        self.label4.place(x=200, y=200)
        
        self.button2 = tk.Button(master, text="Clear All", command=self.clear_items)
        self.button2.place(x=200, y=250)

        self.button3 = tk.Button(master, text="Update Name", command=self.update_name_item)
        self.button3.place(x=200, y=300)

        self.item_list = tk.Listbox(master)
        self.item_list.place(x=350, y=50)
        self.item_list.bind("<<ListboxSelect>>", self.select_item)

        
        self.button3 = tk.Button(master, text="Print Receipt", command=self.print_receipt_button)
        self.button3.place(x=350, y=250)
        
        '''
        self.print_button = tk.Button(master, text="Print Receipt", command=self.print_receipt)
        self.print_button.place(x=200, y=350)
        '''
        self.item_count = 0
        self.item_prices = []
        self.total = 0



    def add_item(self):
        item_name = self.entry1.get()
        item_price = float(self.entry2.get())

        self.item_count += 1
        self.item_prices.append(item_price)
        self.total += item_price

        self.item_list.insert(END, f"{self.item_count}. {item_name} (Rp. {item_price:.2f})")
        self.total_price.set(f"Rp. {self.total:.2f}")

        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        
    def select_item(self, event):
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            item_price = self.item_prices[index]
            self.entry1.delete(0, tk.END)
            self.entry1.insert(tk.END, self.item_list.get(index))
            self.entry2.delete(0, tk.END)
            self.entry2.insert(tk.END, item_price)
        
    def update_name_item(self):
        selected_item = self.item_list.curselection()
        if selected_item:
            new_name = self.entry1.get()
            self.item_list.delete(selected_item)
            self.item_list.insert(selected_item, new_name)
        else:
            messagebox.showinfo("Error", "Please select an item to update.")

    def clear_items(self):
        self.item_list.delete(0, END)
        self.item_count = 0
        self.item_prices = []
        self.total = 0
        self.total_price.set("")

    def submit(self):
        # Get the transaction amount from the entry widget and perform some action
        amount = self.entry.get()
        print(f"Transaction amount: {amount}")
        
    def total_price(self):
        total = 0
        for key, value in self.nama_item.items():
            total += value[0] * value[1]

        if total > 500000:
            total *= 0.9
            diskon = "10%"
        elif total > 300000:
            total *= 0.92
            diskon = "8%"
        elif total > 200000:
            total *= 0.95
            diskon = "5%"
        else:
            diskon = "0%"

        return total, diskon
        
    def print_receipt(self):
        total_harga, diskon = self.total_price()
        total_harga_setelah_diskon = total_harga
        if diskon != "0%":
            total_harga_setelah_diskon = total_harga - (total_harga * float(diskon.strip('%')) / 100)

        receipt = f"===== Struk Belanjaan =====\n"
        receipt += f"ID Customer: {self.id_customer}\n"
        receipt += f"{'Item':<10} {'Jumlah':<10} {'Harga':<10}\n"
        for item in self.nama_item:
            receipt += f"{item:<10} {self.nama_item[item][0]:<10} {self.nama_item[item][1]:<10}\n"
        receipt += f"{'Total Harga':<20} {total_harga.get():<10}\n"
        receipt += f"{'Diskon':<20} {diskon.get()}\n"
        receipt += f"{'Total Harga Setelah Diskon':<20} {total_harga_setelah_diskon}<10\n"
        receipt += f"==========================\n"

        receipt_window = tk.Toplevel()
        receipt_window.title("Struk Belanjaan")
        receipt_window.geometry("500x400")
        receipt_window.resizable(False, False)

        receipt_label = tk.Label(receipt_window, text=receipt, justify="left", anchor="w", font=("Courier", 12))
        receipt_label.pack(padx=20, pady=20)

        receipt_button = tk.Button(receipt_window, text="OK", command=receipt_window.destroy)
        receipt_button.pack(pady=20)

        self.clear_items()


    def print_receipt_button(self):
        # create a new window for the receipt
        receipt_window = tk.Toplevel(self.master)
        receipt_window.title("Receipt")

        # add the receipt text to a Text widget
        receipt_text = tk.Text(receipt_window, height=20, width=50)
        receipt_text.pack()

        receipt = "Receipt:\n"
        for item in self.item_list.get(0, tk.END):
            receipt += f"{item}\n"

        receipt += f"\nTotal: ${self.total:.2f}"
        receipt_text.insert(tk.END, receipt)

        # add a button to close the window
        close_button = tk.Button(receipt_window, text="Close", command=receipt_window.destroy)
        close_button.pack()

