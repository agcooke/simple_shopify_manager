import json
import shopify


def load_shop(filename):
    with open(filename, "r") as f:
        credentials = json.load(f)
        shop_url = "https://%s:%s@%s.myshopify.com/admin/" % (credentials["access_key"], credentials["secret_key"],
                                                              credentials["shop"])
        shopify.ShopifyResource.set_site(shop_url)
        shop = shopify.Shop.current()
    return shop, credentials["shop"]
