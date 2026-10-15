from typing import Literal

ProductDetailScope = Literal["system", "user"]

PRODUCT_DETAIL_SCOPE_VALUES: set[ProductDetailScope] = {
    "system",
    "user",
}


def check_product_detail_scope(value: str) -> ProductDetailScope:
    if value in PRODUCT_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_SCOPE_VALUES!r}")
