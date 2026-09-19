import pandas as pd

"""
Some of the json output includes lists which are not accepted by sqlite db, so needs to be normalised.

The column headings affected are: 
Tags        --> list of possible tags
Dimensions  --> dict of height, width, depth
Reviews     --> list of dicts (rating, comment, date)
Meta        --> dict of createdAt, updateAt, barcode
Images      --> list of URLs 

"""


def transform_products(raw_df):
    df = raw_df.drop(columns=['tags', 'dimensions', 'reviews', 'meta', 'images'])
    df["etl_timestamp"] = pd.Timestamp.now('UTC')
    return df


def normalize_tags(raw_df):
    rows = []
    for _, row in raw_df.iterrows():                        #TODO check iterrows
        if isinstance(row["tags"], list):
            for tag in row["tags"]:
                rows.append({"product_id": row["id"], "tag": tag}) #need product id for each tag 
    return pd.DataFrame(rows)

def normalize_dimensions(raw_df):
    rows = []
    for _, row in raw_df.iterrows():
        dims = row["dimensions"]
        if isinstance(dims, dict):
            rows.append({
                "product_id": row["id"],
                "width": dims.get("width"),
                "height": dims.get("height"),
                "depth": dims.get("depth")
            })
    return pd.DataFrame(rows)

def normalize_reviews(raw_df):
    rows = []
    for _, row in raw_df.iterrows():
        reviews = row["reviews"]
        if isinstance(reviews, list):
            for r in reviews:                       #list of dicts to iterate over 
                rows.append({
                    "product_id": row["id"],
                    "rating": r.get("rating"),      #each review is a dict --> .get()
                    "comment": r.get("comment"),
                    "date": r.get("date")
                })
    return pd.DataFrame(rows)

def normalize_meta(raw_df):
    rows = []
    for _, row in raw_df.iterrows():
        meta = row["meta"]
        if isinstance(meta, dict):
            rows.append({
                "product_id": row["id"],
                "createdAt": meta.get("createdAt"),
                "updatedAt": meta.get("updatedAt"),
                "barcode": meta.get("barcode")
            })
    return pd.DataFrame(rows)

def normalize_images(raw_df):
    rows = []
    for _, row in raw_df.iterrows():
        images = row["images"]
        if isinstance(images, list):
            for img in images:
                rows.append({"product_id": row["id"], "image_url": img})
    return pd.DataFrame(rows)





if __name__ == "__main__": 
    from extract import extract_products
    raw = extract_products()
    transform_products(raw)

