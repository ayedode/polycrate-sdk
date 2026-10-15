from typing import Literal

ProductPublicDetailCriticalityType1 = Literal["", "high", "low", "medium"]

PRODUCT_PUBLIC_DETAIL_CRITICALITY_TYPE_1_VALUES: set[ProductPublicDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_product_public_detail_criticality_type_1(value: str) -> ProductPublicDetailCriticalityType1:
    if value in PRODUCT_PUBLIC_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_DETAIL_CRITICALITY_TYPE_1_VALUES!r}")
