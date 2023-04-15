class Transaction() :
    def __init__(self, id_customer) :
        self.id_customer = id_customer
        self.nama_item = dict()
    
    
    def add_item(self, nama_item, jumlah_item, harga) : #Menambahkan item
        self.nama_item[nama_item] = [jumlah_item, harga] 
   
                
    def total_price(self): #script lebih bertujuan untuk mengecek jumlah total belanjaan
        try :
            total_belanja = 0
            total = 0
            
            for key, value in self.nama_item.items():
                total += value[0] * value[1]
                total_belanja += value[0] * value[1]

            if total > 500000:
                informasi_total = (f"Total belanjaan anda sebesar Rp. {total_belanja}")
                total *= 0.9
                diskon = "10%"
            elif total > 300000:
                informasi_total = (f"Total belanjaan anda sebesar Rp. {total_belanja}")
                total *= 0.92
                diskon = "8%"
            elif total > 200000:
                informasi_total = (f"Total belanjaan anda sebesar Rp. {total_belanja}")
                total *= 0.95
                diskon = "5%"
            else:
                informasi_total = (f"Total belanjaan anda sebesar Rp. {total_belanja}")
                diskon = "0%"
                
            '''
            return yang dikelarkan terdiri dari total belanja dengan keterangan(string), diskon apa yang didapat, 
            total belanja hanya angka(integer) yang telah dipotong diskon, dan nilai total belanja penjumlahan total jumlah brang dan harga (integer)
            Kenapa dikeluarkan 4 nilai ?
            karena return diskon akan dipakai pada method print_receipt bersama dengan nilai total belanja
            '''
            return informasi_total, diskon , total, total_belanja
        
        except Exception as e: 
            print("Error:", e) 
    
    
    
    def print_receipt(self):
        informasi, diskon, total_after, total_before = self.total_price()  #2 nilai yang menjadi sesuai urutan list yaitu diskon dan total_belanja(total_before)
        total_harga_setelah_diskon = total_before #nilai perkalian antara jumlah barang dan harga
        if diskon != "0%":
            total_harga_setelah_diskon = total_before - (total_before * float(diskon.strip('%')) / 100) # untuk mencetak nilai diskon  yang didapat dan harga setelah potonngan diskon

        print(f"===== Struk Belanjaan =====")
        print(f"ID Customer: {self.id_customer}")
        print(f"{'Item':<10} {'Jumlah':<10} {'Harga':<10}")
        for item in self.nama_item:
            print(f"{item:<10} {self.nama_item[item][0]:<10} {self.nama_item[item][1]:<10}")
        print(f"{'Total Harga':<20} {total_before:<10}")
        print(f"{'Diskon':<20} {diskon}")
        print(f"{'Total Harga Setelah Diskon':<20} {total_harga_setelah_diskon:<10}")
        print(f"==========================")