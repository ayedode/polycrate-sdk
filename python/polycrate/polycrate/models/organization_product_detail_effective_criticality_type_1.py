from typing import Literal

OrganizationProductDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ORGANIZATION_PRODUCT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[
    OrganizationProductDetailEffectiveCriticalityType1
] = {
    "high",
    "low",
    "medium",
}


def check_organization_product_detail_effective_criticality_type_1(
    value: str,
) -> OrganizationProductDetailEffectiveCriticalityType1:
    if value in ORGANIZATION_PRODUCT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
