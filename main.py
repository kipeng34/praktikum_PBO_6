from core.notifiers import ConsoleNotifier, EmailNotifier
from core.processor import PaymentProcessor
from plugins.ewallet import EWallet
from plugins.transfer_bank import TransferBank
 
email = "andi@utr.ac.id"
pemroses = PaymentProcessor(ConsoleNotifier())
pemroses.checkout(TransferBank(saldo=1_000_000), 250_000, email)
pemroses.checkout(EWallet(saldo=100_000), 150_000, email)
 
# Ganti kanal notifikasi tanpa mengubah PaymentProcessor
pemroses.notifier = EmailNotifier()
dana = EWallet(saldo=500_000, provider="DANA")
pemroses.checkout(dana, 300_000, email)
 
# Objek yang bukan Notifier harus ditolak
try:
    PaymentProcessor(notifier="bukan notifier")
except TypeError as e:
    print("Error:", e)
