from typing import Literal

OrganizationProductDetailKind = Literal["generic"]

ORGANIZATION_PRODUCT_DETAIL_KIND_VALUES: set[OrganizationProductDetailKind] = {
    "generic",
}


def check_organization_product_detail_kind(value: str) -> OrganizationProductDetailKind:
    if value in ORGANIZATION_PRODUCT_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_KIND_VALUES!r}")
