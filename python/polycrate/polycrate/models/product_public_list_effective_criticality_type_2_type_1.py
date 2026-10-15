from typing import Literal

ProductPublicListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

PRODUCT_PUBLIC_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ProductPublicListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_product_public_list_effective_criticality_type_2_type_1(
    value: str,
) -> ProductPublicListEffectiveCriticalityType2Type1:
    if value in PRODUCT_PUBLIC_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
