from typing import Literal

OrganizationProductDetailCriticalityType1 = Literal["", "high", "low", "medium"]

ORGANIZATION_PRODUCT_DETAIL_CRITICALITY_TYPE_1_VALUES: set[OrganizationProductDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_organization_product_detail_criticality_type_1(value: str) -> OrganizationProductDetailCriticalityType1:
    if value in ORGANIZATION_PRODUCT_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_CRITICALITY_TYPE_1_VALUES!r}"
    )
