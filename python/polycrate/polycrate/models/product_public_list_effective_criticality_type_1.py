from typing import Literal

ProductPublicListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

PRODUCT_PUBLIC_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ProductPublicListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_product_public_list_effective_criticality_type_1(value: str) -> ProductPublicListEffectiveCriticalityType1:
    if value in PRODUCT_PUBLIC_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
