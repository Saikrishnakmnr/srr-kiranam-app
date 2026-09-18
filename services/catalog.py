from services.supabase_client import get_supabase


def _get_rows(table_name):
    supabase = get_supabase()

    if supabase is None:
        return []

    try:
        response = (
            supabase
            .table(table_name)
            .select("*")
            .execute()
        )

        return response.data or []

    except Exception:
        return []


def _first_value(row, names, default=None):
    for name in names:
        if name in row and row[name] is not None:
            return row[name]

    return default


def get_categories():
    rows = _get_rows("kiranam_categories")

    categories = []

    for row in rows:
        category_id = _first_value(
            row,
            ["id", "category_id"],
        )

        category_name = _first_value(
            row,
            ["name", "category_name", "title"],
        )

        if category_name is None:
            continue

        categories.append(
            {
                "id": category_id,
                "name": str(category_name),
            }
        )

    return categories


def get_products(
    category_id=None,
    search=None,
    featured_only=False,
):
    rows = _get_rows("kiranam_products")

    products = []

    for row in rows:
        product_id = _first_value(
            row,
            ["id", "product_id"],
        )

        name = _first_value(
            row,
            ["name", "product_name", "title"],
            "Product",
        )

        price = _first_value(
            row,
            [
                "price",
                "selling_price",
                "sale_price",
            ],
            0,
        )

        mrp = _first_value(
            row,
            [
                "mrp",
                "original_price",
                "list_price",
            ],
            price,
        )

        product_category_id = _first_value(
            row,
            [
                "category_id",
                "category",
                "cat_id",
            ],
        )

        image_url = _first_value(
            row,
            [
                "image_url",
                "image",
                "photo_url",
                "product_image",
            ],
            "",
        )

        description = _first_value(
            row,
            [
                "description",
                "details",
            ],
            "",
        )

        # Search filter
        if search:
            if search.lower() not in str(name).lower():
                continue

        # Category filter
        if category_id is not None:
            if str(product_category_id) != str(category_id):
                continue

        # Featured filter
        if featured_only:
            featured = _first_value(
                row,
                [
                    "is_featured",
                    "featured",
                ],
                False,
            )

            if not featured:
                continue

        products.append(
            {
                "id": product_id,
                "name": str(name),
                "price": price,
                "selling_price": price,
                "mrp": mrp,
                "category_id": product_category_id,
                "image_url": image_url,
                "description": description,
                "is_active": True,
                "raw": row,
            }
        )

    return products


def get_all_products():
    return get_products()


def get_featured_products():
    return get_products(
        featured_only=True
    )


def get_product(product_id):
    products = get_products()

    for product in products:
        if str(product.get("id")) == str(product_id):
            return product

    return None


def get_category_name(category_id):
    categories = get_categories()

    for category in categories:
        if str(category.get("id")) == str(category_id):
            return category.get("name", "")

    return ""


def get_products_with_category():
    products = get_products()

    categories = get_categories()

    category_map = {}

    for category in categories:
        category_id = category.get("id")
        category_name = category.get("name")

        if category_id is not None:
            category_map[str(category_id)] = category_name

    for product in products:
        category_id = product.get("category_id")

        product["category_name"] = category_map.get(
            str(category_id),
            "",
        )

    return products
