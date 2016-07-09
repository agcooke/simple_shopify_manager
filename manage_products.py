#!/usr/bin/env python
"""Manage Shopify Products

Usage:
  manage_products.py <export|update>
"""
from __future__ import print_function
import shopify
from simple_shopify import credentials
from simple_shopify import storage
import argparse

import simple_shopify.meta_field as meta_field
import simple_shopify.simple_product as simple_product

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('command', type=str,
                        help='<download|update>')
    parser.add_argument('--file', "-f", dest='data_file', required=True,
                        help='The data file to use for import or download')
    parser.add_argument('--credentials', "-c", dest='credentials_file', default="./credentials.json",
                        help='The shopify store credentials json file.')
    arguments = parser.parse_args()
    download = arguments.command == "download"
    update = arguments.command == "update"
    data_file = arguments.data_file
    credentials_file = arguments.credentials_file

    shop, shop_name = credentials.load_shop(credentials_file)
    namespace = shop_name

    if download:
        print("Downloading Products")
        products = shopify.Product.find(limit=250)
        print("'%s' Products downloaded" % len(products))
        product_data = [simple_product.SimpleProduct(product) for product in products]
        product_data, max_lens = meta_field.resolve_meta_fields(product_data, namespace)
        storage.write(data_file, product_data, max_lens)
    elif update:
        print("Reading Products from '%s'" % data_file)
        products = storage.read(data_file)
        print("Products read.")
        print("Updating meta_fields in namespace '%s'." % namespace)
        for product in products:
            print(".", end="")
            meta_field.update_meta_fields(product, namespace=shop_name)
        print("\nMeta_fields updated.")
