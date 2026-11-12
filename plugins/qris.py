from core.base import PaymentMethod
from core.registry import register_plugin
from core.utils import buat_id
 
 
@register_plugin("qris")
class QRIS(PaymentMethod):
    BATAS_TRANSAKSI = 5_000_000
 
    def __init__(self, merchant: str = "Kantin Kampus"):
        super().__init__(f"QRIS {merchant}")
        self.merchant = merchant
        
    def biaya_admin(self, jumlah: float) -> float:
        return jumlah * 0.007
 
    def validasi(self, jumlah: float) -> bool:
        return jumlah <= self.BATAS_TRANSAKSI
 
    def bayar(self, jumlah: float) -> str:
        ...  # TODO: kembalikan ID transaksi berawalan "QRS"
        return buat_id("QRS")