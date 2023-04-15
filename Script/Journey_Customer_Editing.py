from Journey_Customer_Baseline import Transaction

'''
Class Editing_tools dibuat untuk memenuhi skema ketika client/pembeli ingin merevisi item,
sehingga dibuat script class secara sistem pewarisan/Inheritance
'''

class Editing_tools(Transaction) :
    def __init__(self, id_customer):
        super().__init__(id_customer)
    
    
    def update_name_item(self, nama_item, new_name): #update name item jika ada salah input
        try :
            if nama_item in self.nama_item:
                self.nama_item[new_name] = self.nama_item.pop(nama_item)
            else :
                raise ValueError(f"Item {nama_item} tidak ditemukan")
            
        except ValueError as ve :
            print(ve)


    def update_jumlah_item(self, nama_item, new_jumlah): #update jumlah item jika ada salah input
        try:
            if nama_item in self.nama_item:
                self.nama_item[nama_item][0] = new_jumlah
            else:
                raise ValueError(f"Item {nama_item} tidak ditemukan.")
            
        except ValueError as ve:
            print(ve)
          
            
    def update_harga(self, nama_item, new_harga): #update harga item jika ada salah input
        if nama_item in self.nama_item:
            self.nama_item[nama_item][1] = new_harga            
                   
    def update_item(self, nama_item): #untuk mengecek key pada dictionary item
        for key in self.nama_item:
            if key == nama_item:
                return key
        return None
    
    
    def delete_item(self, nama_item): #Untuk menghapus 1 row pesanan
        try :
            if nama_item in self.nama_item:
                del self.nama_item[nama_item]
                print(f"Item {nama_item} berhasil dihapus.")
            else:
                raise(f"Tidak ditemukan item dengan nama {nama_item}.")
            
        except ValueError as ve :
            print(ve)
         