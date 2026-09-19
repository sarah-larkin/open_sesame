from extract import extract_products
from transform import *
from load import *

raw = extract_products()   #json
raw_df = pd.DataFrame(raw["products"]) #df

products_df = transform_products(raw_df)  #df
tags_df = normalize_tags(raw_df)
dimensions_df = normalize_dimensions(raw_df)
reviews_df = normalize_reviews(raw_df)
meta_df = normalize_meta(raw_df)
images_df = normalize_images(raw_df)

load_table(products_df, "products")     #sqlite tables
load_table(tags_df, "product_tags")
load_table(dimensions_df, "product_dimensions")
load_table(reviews_df, "product_reviews")
load_table(meta_df, "product_meta")
load_table(images_df, "product_images")


