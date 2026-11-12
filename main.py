from core.base import PaymentMethod
from plugins.transfer_bank import TransferBank
 
# Eksperimen A: ABC tidak boleh diinstansiasi langsung
try:
    PaymentMethod("uji")
except TypeError as e:
    print("Error yang diharapkan:", e)
 
 
# Eksperimen B: subclass yang belum lengkap (bayar() belum ada)
class Setengah(PaymentMethod):
    def validasi(self, jumlah):
        return True
 
 
try:
    Setengah("uji")
except TypeError as e:
    print("Error yang diharapkan:", e)
 
# Eksperimen C: subclass lengkap berjalan normal
transfer = TransferBank(saldo=500_000, bank="BCA")
print("ID transaksi:", transfer.proses(150_000))
print("Saldo sisa  :", transfer.saldo)
