from typing import Literal

RegistrarTLDPriceDetailCriticalityType2Type1 = Literal["", "high", "low", "medium"]

REGISTRAR_TLD_PRICE_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[RegistrarTLDPriceDetailCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_registrar_tld_price_detail_criticality_type_2_type_1(
    value: str,
) -> RegistrarTLDPriceDetailCriticalityType2Type1:
    if value in REGISTRAR_TLD_PRICE_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
