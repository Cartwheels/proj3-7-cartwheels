import os

# Application
SECRET_KEY = "}. 2}MpuI3J[yYGg8*b9jL&;%Lyt(WhxxhlFaoadm}sQjaVF+/z`vs~#qd@ Spd8"
STRIPE_SECRET_KEY = "sk_test_o6tpz20D63VVmP8USt1TMB9K"
STORE_FILE = "website/settings/store.info"
DIST_OFFSET = 0.01

# Mongodb
MONGO_URL = os.environ.get('MONGOHQ_URL')

DB_NAME = 'cartwheels'

COLLECTIONS = {
        'User': 'users',
        'Cart': 'carts',
        'Tag': 'tags',
        'Review': 'reviews',
        'Photo': 'photos',
        'CartAd': 'ads',
        'Collection': 'ignore'
        }

IGNORE_ATTRS = ['_obj', 'collection', 'fs', 'db']
