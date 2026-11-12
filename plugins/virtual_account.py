from datetime import datetime, timedelta

from core.base import PaymentMethod
from core.registry import register_plugin
from core.utils import buat_id


@register_plugin("va")
class VirtualAccount(PaymentMethod):
    def __init__(self, bank: str = "Mandiri", batas_jam: int = 24):
        super().__init__(f"Virtual Account {bank}")
        self.status = "menunggu"
        self.batas_waktu = datetime.now() + timedelta(hours=batas_jam)

    def biaya_admin(self, jumlah: float) -> float:
        return 4000

    def validasi(self, jumlah: float) -> bool:
        return jumlah >= 10_000 and datetime.now() <= self.batas_waktu

    def bayar(self, jumlah: float) -> str:
        self.status = "menunggu"
        return buat_id("VA")