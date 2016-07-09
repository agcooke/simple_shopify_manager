from __future__ import print_function
import shopify


META_TAG = "META:"


def resolve_meta_fields(product_data, namespace):
    print("Downloading meta fields")
    max_lens = {}
    for product in product_data:
        meta_fields = shopify.Metafield.find(resource='products', namespace=namespace, resource_id=product.id)
        print(".", end="")
        for field in meta_fields:
            values = field.value.split("|")
            if len(values) > max_lens.get(field.key, 0):
                max_lens[field.key] = len(values)

            product.meta_fields[field.key] = values
    print("\nDownloaded '%s' product's meta fields" % len(product_data))
    return product_data, max_lens


def pad_list(values, max_len):
    return values[:max_len] + ["", ] * (max_len - len(values))


def update_meta_fields(product, namespace):
        for field in product.meta_fields.keys():
            values = "|".join(product.meta_fields[field])
            meta_field = shopify.Metafield({'value_type': 'string', 'namespace': namespace, 'value': values,
                                            'key': field, 'resource': 'products', 'resource_id': product.id})
            meta_field.save()
