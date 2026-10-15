from typing import Literal

OrganizationProductDetailScope = Literal["system", "user"]

ORGANIZATION_PRODUCT_DETAIL_SCOPE_VALUES: set[OrganizationProductDetailScope] = {
    "system",
    "user",
}


def check_organization_product_detail_scope(value: str) -> OrganizationProductDetailScope:
    if value in ORGANIZATION_PRODUCT_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_SCOPE_VALUES!r}")
