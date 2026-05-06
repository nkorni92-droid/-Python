from smartphone import Smartphone
catalog = []
catalog.append(Smartphone("Apple", "iPhone 14", "+7 999 111-22-33"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+7 999 222-33-44"))
catalog.append(Smartphone("Nokia", "G60", "+7 999 333-44-55"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+7 999 444-55-66"))
catalog.append(Smartphone("Sony", "Xperia 1 V", "+7 999 555-66-77"))
for Smartphone in catalog:
    print(f"{Smartphone.brand} - {Smartphone.model}. {Smartphone.subscriber_number}")