from core.protocols import Notifier
from core.notifiers import ConsoleNotifier, EmailNotifier, WhatsAppNotifier
 
 
class TanpaKirim:
    """Kelas ini sengaja tidak punya method kirim()."""
 
 
daftar = [
    ConsoleNotifier(),
    EmailNotifier(),
    WhatsAppNotifier(),
    TanpaKirim(),
]
for n in daftar:
    cocok = isinstance(n, Notifier)
    print(f"{type(n).__name__:<16} memenuhi Notifier? {cocok}")
