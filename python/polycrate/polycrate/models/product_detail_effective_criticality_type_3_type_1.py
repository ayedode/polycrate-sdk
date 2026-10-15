from typing import Literal

ProductDetailEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

PRODUCT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ProductDetailEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_product_detail_effective_criticality_type_3_type_1(value: str) -> ProductDetailEffectiveCriticalityType3Type1:
    if value in PRODUCT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
