from typing import Literal

PatchedOrganizationProductDetailRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_ORGANIZATION_PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PatchedOrganizationProductDetailRequestCriticalityType2Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_organization_product_detail_request_criticality_type_2_type_1(
    value: str,
) -> PatchedOrganizationProductDetailRequestCriticalityType2Type1:
    if value in PATCHED_ORGANIZATION_PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ORGANIZATION_PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
