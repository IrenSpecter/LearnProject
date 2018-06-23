# price = 180
# vat_rate = 18
# vat=price/100*vat_rate
# print(vat)
def get_vat(price,vat_rate):
    vat=price/100*vat_rate
    price_no_vat=price-vat
    print(price_no_vat)
price1=100
vat_rate1=18
get_vat(price1,vat_rate1)

price2=500
vat_rate2=10
get_vat(price2,vat_rate2)

get_vat(50,'5')
get_vat(-100,18)
