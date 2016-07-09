# Simple Shopify Manager

This project is a simple tool that is being created to help manage the [LPRD Design website](http://lprd.design)

It is very limited at the moment and will grow over time.

# Limitations

- Only supports up to 250 products.
- Can only manage Meta Fields.

# Meta field management
- `manage_products.py download -f output.csv` - Downloads you products into a CSV file with meta fields.
- After download you can edit the csv.
- `manage_products.py upload -f output.csv` - Updates the meta fields in Shopify.

# Credentials

The script `manage_products.py` needs a `credentials.json` file to work. You get the
credentials from shopify by creating a "Private App".

The format of the file is as follows:


    {
      "shop":"<your shop name>",
      "access_key": "<first hash>",
      "secret_key": "<second hash>"
    }

# License
Use as you like, its untested minimally useful, so do not expect too much. Open bug reports and
happily submit Pull requests if you have some updates.