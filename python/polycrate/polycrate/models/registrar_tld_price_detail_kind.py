from typing import Literal

RegistrarTLDPriceDetailKind = Literal["generic"]

REGISTRAR_TLD_PRICE_DETAIL_KIND_VALUES: set[RegistrarTLDPriceDetailKind] = {
    "generic",
}


def check_registrar_tld_price_detail_kind(value: str) -> RegistrarTLDPriceDetailKind:
    if value in REGISTRAR_TLD_PRICE_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_DETAIL_KIND_VALUES!r}")
