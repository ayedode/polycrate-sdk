from typing import Literal

RegistrarTLDPriceDetailCreatedByComponentType3Type1 = Literal["", "api", "cli", "operator"]

REGISTRAR_TLD_PRICE_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES: set[
    RegistrarTLDPriceDetailCreatedByComponentType3Type1
] = {
    "",
    "api",
    "cli",
    "operator",
}


def check_registrar_tld_price_detail_created_by_component_type_3_type_1(
    value: str,
) -> RegistrarTLDPriceDetailCreatedByComponentType3Type1:
    if value in REGISTRAR_TLD_PRICE_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_DETAIL_CREATED_BY_COMPONENT_TYPE_3_TYPE_1_VALUES!r}"
    )
