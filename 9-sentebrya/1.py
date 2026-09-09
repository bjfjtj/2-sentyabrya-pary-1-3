class Goods:
    title = "Мороженое"
    weight = 150
    tp = "Еда"
    price = 100

# Изменяем price и добавляем inflation через setattr
setattr(Goods, 'price', 2048)
setattr(Goods, 'inflation', 100)