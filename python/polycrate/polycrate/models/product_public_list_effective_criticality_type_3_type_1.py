from typing import Literal

ProductPublicListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

PRODUCT_PUBLIC_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ProductPublicListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_product_public_list_effective_criticality_type_3_type_1(
    value: str,
) -> ProductPublicListEffectiveCriticalityType3Type1:
    if value in PRODUCT_PUBLIC_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
