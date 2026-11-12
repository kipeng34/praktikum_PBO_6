from core.notifiers import ConsoleNotifier
from core.protocols import Notifier
from core.processor import PaymentProcessor
from core.registry import buat_metode, daftar_plugin
from core.utils import rupiah
from plugins import muat_semua_plugin
from core.utils import buat_id
from core.notifiers import TelegramNotifier
from plugins.qris import QRIS
 
tg = TelegramNotifier()
print("Memenuhi Notifier?", isinstance(tg, Notifier))  # Harus True

pemroses = PaymentProcessor(tg)
pemroses.checkout(QRIS(), 50_000, "mahasiswa@utr.ac.id")
def main() -> None:
    muat_semua_plugin()
    print("Plugin terdaftar:", daftar_plugin())
    print("-" * 60)
 
    pemroses = PaymentProcessor(ConsoleNotifier())
 
    skenario = [
        ("transfer", {"saldo": 1_000_000, "bank": "BCA"}, 250_000),
        ("ewallet", {"saldo": 100_000}, 150_000),
        ("ewallet", {"saldo": 5_000_000}, 2_500_000),
        ("qris", {}, 50_000),
    ]
 
    for kode, parameter, jumlah in skenario:
        try:
            metode = buat_metode(kode, **parameter)
        except KeyError as err:
            print("[PERINGATAN]", err)
            continue
        pemroses.checkout(metode, jumlah, pelanggan="mahasiswa@utr.ac.id")
 
    print("-" * 60)
    print("Riwayat transaksi berhasil:")
    for trx_id, nama, jumlah in pemroses.riwayat:
        print(f"  {trx_id} | {nama} | {rupiah(jumlah)}")
 
 
if __name__ == "__main__":
    main()
