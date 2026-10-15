from typing import Literal

ProductDetailCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PRODUCT_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ProductDetailCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_product_detail_criticality_type_3_type_1(value: str) -> ProductDetailCriticalityType3Type1:
    if value in PRODUCT_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
