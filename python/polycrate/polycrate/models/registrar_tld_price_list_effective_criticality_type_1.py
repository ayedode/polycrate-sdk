from typing import Literal

RegistrarTLDPriceListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

REGISTRAR_TLD_PRICE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[RegistrarTLDPriceListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_registrar_tld_price_list_effective_criticality_type_1(
    value: str,
) -> RegistrarTLDPriceListEffectiveCriticalityType1:
    if value in REGISTRAR_TLD_PRICE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
