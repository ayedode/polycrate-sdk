from typing import Literal

OrganizationProductDetailEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

ORGANIZATION_PRODUCT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    OrganizationProductDetailEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_organization_product_detail_effective_criticality_type_2_type_1(
    value: str,
) -> OrganizationProductDetailEffectiveCriticalityType2Type1:
    if value in ORGANIZATION_PRODUCT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
