import simple_shopify.meta_field


class SimpleProduct(object):

    def __init__(self, product=None, product_id=None, title=None):
        if product:
            self.id = product.id
            self.title = product.title
            self.meta_fields = {}
        else:
            self.id = product_id
            self.title = title
            self.meta_fields = {}

    def pad_field(self, field, max_len):
        values = self.meta_fields.get(field, [])
        values = simple_shopify.meta_field.pad_list(values, max_len)
        self.meta_fields[field] = values

    def to_list(self):
        meta_fields = sorted(self.meta_fields.keys())
        the_list = [self.title, self.id]
        for meta_field in meta_fields:
            the_list.append(simple_shopify.meta_field.META_TAG + meta_field)
            the_list = the_list + self.meta_fields[meta_field]
        return the_list

    def __str__(self):
        return str(self.to_list())
