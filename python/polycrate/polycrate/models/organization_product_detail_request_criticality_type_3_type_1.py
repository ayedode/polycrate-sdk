from typing import Literal

OrganizationProductDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

ORGANIZATION_PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    OrganizationProductDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_organization_product_detail_request_criticality_type_3_type_1(
    value: str,
) -> OrganizationProductDetailRequestCriticalityType3Type1:
    if value in ORGANIZATION_PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
