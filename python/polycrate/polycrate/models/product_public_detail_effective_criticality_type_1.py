from typing import Literal

ProductPublicDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

PRODUCT_PUBLIC_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ProductPublicDetailEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_product_public_detail_effective_criticality_type_1(
    value: str,
) -> ProductPublicDetailEffectiveCriticalityType1:
    if value in PRODUCT_PUBLIC_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
