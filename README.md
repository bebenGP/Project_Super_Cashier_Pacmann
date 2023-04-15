# Project Super Cashier - Kelas Statistics - Pacmann
Project ini merupakan hasil belajar materi python di program kelas Statistics - Pacmann

# Customer Journey - Simple Modul Sales

Modul ini digunakan untuk menjadi alat yang diibaratkan seperti POS (Point of Sale), yang teknis penggunaannya yaitu *Self Services*. Modul ini dibuat dengan konsep **Inheritance/Pewarisan** pada OOP (*Object Oriented Programming*) 

Terdapat 2 Class yaitu : 

> a. (Journey_Customer_Baseline) - sebagai **Parent Class**

> b. (Journey_Customer_Editing) - sebagai **Child Class** 

Berikut adalah teknis penggunaan dari modul Customer Journey :

## Pembagian class 
Karena menggunakan konsep Inheritance untuk memanggil kelas dan melakukan banyak pengolahan seperti jika terdapat problem atau kesalahan input barang perlu dilakukan editing item, maka disarankan langsung memakai class **Journey_Customer_Editing** yang didalamnya terdapat method untuk mengedit item.

```
from Journey_Customer_Editing import Editing_tools
from Journey_Customer_Baseline import Transaction
```

## Menambahkan item
Untuk menambahkan item dapat menggunakan method **add_item**
dengan skema pertama lakukan inisiasi sebagai ID Customer, lalu didalam methode add_item terdapat instance yang berisi (nama_item, Jumlah_item, harga)

```
customer = Editing_tools('Beben_01')
customer.add_item('Pepsodent', 3, 8000)
```

## Checking Item
Data yang diinput sebaiknya dilakukan perlu dilakukan pengecekan apakah sudah masuk kedalam sistem/terdaftar didalam class

```
customer.nama_item
```

**output** :
```
{'Pepsodent': [3, 8000]}
```


## Tambahkan kembali item
Karena item yang dimasukkan masukkan masih sedikit, maka sebaiknya ditambah kembali sesuai kebutuhan dari client/pembeli

```
customer.add_item('Sarden', 2, 12000)
customer.add_item('Beras Grade B', 1, 150000)
customer.add_item('Sabun Cair', 2, 40000)
customer.add_item('Rinso', 3, 18000)
customer.add_item('Mie Instans indiemie', 12, 3500)
customer.add_item('Chitatoz', 2, 20000)
```
**output** :
```
{'Pepsodent': [3, 8000],
 'Sarden': [2, 12000],
 'Beras Grade B': [1, 150000],
 'Sabun Cair': [2, 40000],
 'Rinso': [3, 18000],
 'Mie Instans indiemie': [12, 3500],
 'Chitatoz': [2, 20000]}
 ```

## Melakukan Editing - Update name item
Jika semisalnya client/pembeli terjadi kesalahan menginputkan data, maka item yang telah terinput harus diedit kembali. Ini dapat dilakukan dengan menggunakan method **update_name_item**

```
customer.update_name_item('Mie Instans indiemie', 'Mie Instan sedapz')
customer.nama_item
```
**output** :
```
{'Pepsodent': [3, 8000],
 'Sarden': [2, 12000],
 'Beras Grade B': [1, 150000],
 'Sabun Cair': [2, 40000],
 'Rinso': [3, 18000],
 'Chitatoz': [2, 20000],
 'Mie Instan sedapz': [12, 3500]}
 ```

### Melakukan Editing - Jumlah item, update harga
Modul ini juga menyediakan method untuk melakukan editing pada jumlah item dan harga, jika terjadi kesalahan maka dapat langsung diperbaiki dengan menggunakan **"update_jumlah_item"** dan **"update_harga"**.

```
customer.update_jumlah_item('Pepsodent', 2)
customer.update_harga('Chitatoz', 18000)

customer.nama_item
```

**output** :
```
{'Pepsodent': [2, 8000],
 'Sarden': [2, 12000],
 'Beras Grade B': [1, 150000],
 'Sabun Cair': [2, 40000],
 'Rinso': [3, 18000],
 'Chitatoz': [2, 18000],
 'Mie Instan sedapz': [12, 3500]}
 ```
### Deleting Item
Selain bisa menghapus per sub item, modul ini juga bisa menghapus satu row/item secara langsung dengan menggunakan method **delete_item**

```
customer.delete_item('Sarden')
```

**output** :
```
Item Sarden berhasil dihapus.
```
## Menghitung total belanja
Untuk method ini tidak perlu dipanggil/digunakan, karena pada dasarnya method ini dibuat hanya untuk menyematkan metodelogi menghitung dan mendapatkan list index dari perhitungan total belanja terhadap diskon. Method dapat digunakan dengan menggunakan **"total_price"**

```
customer.total_price()
```
**output** :
``` 
('Total belanjaan anda sebesar Rp. 378000', '8%', 347760.0, 378000)
```

1. list pertama adalah comment string sebagai informasi total harga setelah diskon 
2. list kedua string yang menunjukkan besaran diskon yang didapat dengan aturan sebagai berikut :
    + Jika total belanja diatas Rp 200.000 maka akan mendapatkan diskon 5%
    + Jika total belanja diatas Rp 300.000 maka akan mendapatkan diskon 8%
    + Jika total belanja diatas Rp 500.000 maka akan mendapatkan diskon 10%
3. list ketiga adalah total belanjaan yang belum dikurangi dengan diskon yang didapat
4. list keempat yaitu jumlah total belanja setelah di diskon

kenapa dikeluarkan 4 list ? 
> Karena nilai tersebut akan dipakai dalam generate receipt/struk belanjaan

## Print Nota - Struk belanja
Method ini memiliki konsep yang hampir mirip dengan mesin kasir di supermarket yang setiap pembayaran pembelian tiap item maka akan mendaatkan struk belanjaan, untuk menggunakan method ini dapat menggunakan method "**print_receipt**"

```
customer.print_receipt()
```

**output** :
```
===== Struk Belanjaan =====
ID Customer: Beben_01
Item       Jumlah     Harga     
Pepsodent  2          8000      
Beras Grade B 1          150000    
Sabun Cair 2          40000     
Rinso      3          18000     
Chitatoz   2          18000     
Mie Instan sedapz 12         3500      
Total Harga          378000    
Diskon               8%
Total Harga Setelah Diskon 347760.0  
==========================
```

## Customer Journey - GUI
Selain bisa digunakan dengan scripting python, metodelogi dari Customer Journey juga bisa dibuatkan dalam bentuk user interface yang interaktif, dengan menggunakan class **TranscationGUI** 

```
# membuat instance dari class TransactionGUI
root = tk.Tk()
app = TransactionGUI(root)

# menjalankan mainloop dari tkinter
root.mainloop()
```
![TransactionGUI.png](https://github.com/bebenGP/Project_Super_Cashier_Pacmann/blob/master/Picture/TransactionGUI.png)





