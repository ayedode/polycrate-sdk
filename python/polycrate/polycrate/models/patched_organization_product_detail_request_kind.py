from typing import Literal

PatchedOrganizationProductDetailRequestKind = Literal["generic"]

PATCHED_ORGANIZATION_PRODUCT_DETAIL_REQUEST_KIND_VALUES: set[PatchedOrganizationProductDetailRequestKind] = {
    "generic",
}


def check_patched_organization_product_detail_request_kind(value: str) -> PatchedOrganizationProductDetailRequestKind:
    if value in PATCHED_ORGANIZATION_PRODUCT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ORGANIZATION_PRODUCT_DETAIL_REQUEST_KIND_VALUES!r}"
    )
