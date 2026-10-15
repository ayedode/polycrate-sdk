from typing import Literal

OrganizationProductDetailRequestKind = Literal["generic"]

ORGANIZATION_PRODUCT_DETAIL_REQUEST_KIND_VALUES: set[OrganizationProductDetailRequestKind] = {
    "generic",
}


def check_organization_product_detail_request_kind(value: str) -> OrganizationProductDetailRequestKind:
    if value in ORGANIZATION_PRODUCT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_REQUEST_KIND_VALUES!r}")
