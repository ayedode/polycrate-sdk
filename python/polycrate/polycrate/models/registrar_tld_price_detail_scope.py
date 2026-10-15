from typing import Literal

RegistrarTLDPriceDetailScope = Literal["system", "user"]

REGISTRAR_TLD_PRICE_DETAIL_SCOPE_VALUES: set[RegistrarTLDPriceDetailScope] = {
    "system",
    "user",
}


def check_registrar_tld_price_detail_scope(value: str) -> RegistrarTLDPriceDetailScope:
    if value in REGISTRAR_TLD_PRICE_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_DETAIL_SCOPE_VALUES!r}")
