from typing import Literal

RegistrarTLDPriceDetailEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

REGISTRAR_TLD_PRICE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    RegistrarTLDPriceDetailEffectiveCriticalityType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_registrar_tld_price_detail_effective_criticality_type_3_type_1(
    value: str,
) -> RegistrarTLDPriceDetailEffectiveCriticalityType3Type1:
    if value in REGISTRAR_TLD_PRICE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
