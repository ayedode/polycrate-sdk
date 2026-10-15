from typing import Literal

OrganizationProductListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ORGANIZATION_PRODUCT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[OrganizationProductListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_organization_product_list_effective_criticality_type_1(
    value: str,
) -> OrganizationProductListEffectiveCriticalityType1:
    if value in ORGANIZATION_PRODUCT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
