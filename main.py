from amazon import search_amazon
from trendyol_run import search_trendyol
from hepsiburada_run import search_hepsiburada

search_term = "Apple iphone 16 1tb"

#products_trendyol = search_trendyol(search_term)
#products_hepsiburada = search_hepsiburada(search_term)
products_amazon = search_amazon(search_term)

#all_products = products_trendyol + products_hepsiburada + products_amazon

#for p in all_products:
#    print(f"Ürün: {p['name']} - Fiyat: {p['price']}")


