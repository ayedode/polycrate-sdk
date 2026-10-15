from typing import Literal

ProductPublicDetailScope = Literal["system", "user"]

PRODUCT_PUBLIC_DETAIL_SCOPE_VALUES: set[ProductPublicDetailScope] = {
    "system",
    "user",
}


def check_product_public_detail_scope(value: str) -> ProductPublicDetailScope:
    if value in PRODUCT_PUBLIC_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_DETAIL_SCOPE_VALUES!r}")
