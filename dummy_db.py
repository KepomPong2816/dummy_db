import random
from datetime import datetime, date, timedelta

# Define the date range for tgl_pesan
start_date = date(2023, 1, 2) # Need update for date < datetime
end_date = date(2023, 10, 23) # Need update for date < datetime

# Define the id_mobil to harga mapping
harga_map = {
    31: 450000,
    32: 1480000,
    33: 760000,
    27: 600000,
    28: 2500000,
    24: 800000,
    23: 600000,
    25: 1200000,
    26: 500000,
    29: 980000,
    30: 1100000,
}

# Primary key (Auto Increment)
id_transaksi = 0 # First index is 0

# Total data dummy need :
X = 100 # Update manual <<< EDIT THIS !!! <<< Depend on structure table, null value is not recommended for use 

with open("dummy_transaksi.sql", "w") as f:
    for value in range(X):
        if id_transaksi == "null" :
            id_transaksi = "null" # Null
        else :
            id_transaksi += 1 # (x + 1) 
            
        id_cust = random.randint(1, 7) # Range 1 - 7 from Foreign Key
        id_peg = random.randint(15, 17) # Range 15 - 17 from Foreign Key
        id_mobil = random.randint(23, 33) # Range 23 - 33 from Foreign Key
        tgl_pesan = start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) # Random Date between Start-End_date 
        tgl_sewa = tgl_pesan + timedelta(days=1) # +1 Day from tgl_pesan
        tgl_kembali = tgl_sewa + timedelta(days=random.randint(1, 14)) # Approx Range 1 - 14 Days from tgl_sewa        
        status = 'Dipinjam' if tgl_pesan >= date(2023, 10, 10) else 'Selesai' # Status value "Dipinjam" or "Selesai" For Transaction
        cost = (tgl_kembali - tgl_sewa).days * harga_map.get(id_mobil, 0) # (tgl_kembali - tgl_sewa) * 'map_mobil'
        denda = random.randint(100000, 1000000) if random.random() <= 0.05 else 0 # Generate random penalty for <= 5% data dummy, with range 100000 - 1000000
        
        # Need update for date < datetime, currently use manual time with random generate
        sewa_hours = random.randint(9, 16) # Range 9 - 16
        kembali_hours = random.randint(13, 19) # Range 13 - 19
        minutes = str(random.randint(0, 59)).zfill(2) # Range 00 - 59
        seconds = str(random.randint(0, 59)).zfill(2) # Range 00 - 59
        waktu_sewa = f"{sewa_hours}:{minutes}:{seconds}" # HH:MM:SS
        waktu_kembali = f"{kembali_hours}:{minutes}:{seconds}" # HH:MM:SS
          
        # Query Value
        sql_statement = f"({id_transaksi},'{id_cust}','{id_peg}','{id_mobil}','{tgl_pesan}','{tgl_sewa} {waktu_sewa}','{tgl_kembali} {waktu_kembali}','{status}','{cost}','{denda}')"
        if value < X - 1:
            endpoint = ","
        else:
            endpoint = ";"
    
        # Print SQL Value
        f.write(sql_statement+endpoint+"\n")

# Just a message when program is done
print("SQL insert statements value have been saved to dummy_transaksi.sql") 


# error found for this code bellow, make new!!

# Define the date range for tgl_pesan
#start_date = date(2023, 1, 2)
#end_date = date(2023, 10, 23)

# start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
# end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

# d = datetime.today()
# d = d.replace(hour=0, minute=0, second=0, microsecond=0)

# Define the id_mobil to harga mapping
#harga_map = {
#    31: 450000,
 #   33: 760000,
  #  27: 600000,
   # 28: 2500000,
    #24: 800000,
    #23: 600000,
   # 25: 1200000,
  #  26: 500000,
 #   29: 980000,
#    30: 1100000,
#}

#with open("dummy_transaksi.sql", "w") as f:
 #   for _ in range(10000000):
  #      id_transaksi = 13   
   #     id_cust = random.randint(1, 7)
    #    id_peg = random.randint(15, 17)
     #   id_mobil = random.randint(23, 33)
      #  tgl_pesan = start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) #fix delete %H%M%S 
       # tgl_sewa = tgl_pesan + timedelta(days=1) #fix delete %H%M%S 
        #sewa_hours = random.randint(9, 16)
        #kembali_hours = random.randint(13, 19)
        #minutes = random.randint(0, 59)
        #seconds = random.randint(0, 59)
        #waktu_sewa = f"{sewa_hours}:{minutes}:{seconds}"
        #tgl_kembali = tgl_sewa + timedelta(days=random.randint(1, 14)) #fix delete %H%M%S 
        #waktu_kembali = f"({kembali_hours}:{minutes}:{seconds})"
#        status = 'Dipinjam' if tgl_pesan >= datetime(2023, 10, 10) else 'Selesai'
 #       cost = (tgl_kembali - tgl_sewa).days * harga_map.get(id_mobil, 0)
  ##     sql_statement = f"({id_transaksi},'{id_cust}','{id_peg}','{id_mobil}','{tgl_pesan}','{tgl_sewa} {waktu_sewa}','{tgl_kembali} {waktu_kembali}','{status}','{cost}','{denda}'),\n"
    #    f.write(sql_statement)
        
#print("SQL insert statements have been saved to dummy_transaksi.sql")