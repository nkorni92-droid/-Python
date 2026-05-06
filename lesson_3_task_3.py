from Address import Address
from Mailing import Mailing
from_address = Address(
    "101000", 
    "Москва", 
    "Тверская", 
    "10", 
    "42"
)
to_address = Address(
    "190000", 
    "Санкт-Петербург", 
    "Невский проспект", 
    "25", 
    "15"
)
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350.50,
    track="TRK123456789"
)
print(
    f"Отправление {mailing.track} "
    f"из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в {mailing.to_address.index}, "
    f"{mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)