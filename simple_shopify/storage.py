import csv
import datetime
import os
import shutil

from simple_shopify.meta_field import META_TAG, pad_list
from simple_shopify.simple_product import SimpleProduct


def write(data_file, product_data, max_lens):
    product_data = _pad_meta_fields(max_lens, product_data)

    matrix = [product.to_list() for product in product_data]
    matrix_transpose = zip(*matrix)

    if os.path.isfile(data_file):
        timestamp = str(datetime.datetime.now()).replace(" ", "-")
        back_up_datafile = "%s.backup.%s.csv" % (data_file, timestamp)
        shutil.copy(data_file, back_up_datafile)
        print("'%s' backed up to '%s'" % (data_file, back_up_datafile))

    print("Writing Data to %s" % data_file)
    with open(data_file, "w") as fp:
        w = csv.writer(fp)
        for row in matrix_transpose:
            w.writerow(row)
    print("Data written to %s" % data_file)


def read(data_file):
    raw_products = []
    with open(data_file, "r") as fp:
        r = csv.reader(fp)
        for row in r:
            raw_products.append(row)
    raw_products = zip(*raw_products)
    products = []
    for raw_product in raw_products:
        product = SimpleProduct(product_id=raw_product[1], title=raw_product[0])
        for item in raw_product[2:]:
            if item.startswith(META_TAG):
                field = item[len(META_TAG):]
            else:
                values = product.meta_fields.get(field, [])
                values.append(item)
                values = filter(lambda x: x != "", values)
                if values:
                    product.meta_fields[field] = values
        products.append(product)
        print(" -- %s" % str(product))
    return products


def _pad_meta_fields(max_lens, product_data):
    for field in max_lens.keys():
        max_len = max_lens[field]
        for product in product_data:
            values = product.meta_fields.get(field, [])
            values = pad_list(values, max_len)
            product.meta_fields[field] = values
    return product_data



