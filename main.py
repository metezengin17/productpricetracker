from trendyol_run import search_trendyol
from hepsiburada_run import search_hepsiburada

search_term = "Apple iphone 16 1tb"
products_trendyol = [] # bunu sonra sil
products_trendyol = search_trendyol(search_term)
products_hepsiburada = search_hepsiburada(search_term)

all_products = products_trendyol + products_hepsiburada

for p in all_products:
    print(f"Ürün: {p['name']} - Fiyat: {p['price']}")


