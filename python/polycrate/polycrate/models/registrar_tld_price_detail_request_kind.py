from typing import Literal

RegistrarTLDPriceDetailRequestKind = Literal["generic"]

REGISTRAR_TLD_PRICE_DETAIL_REQUEST_KIND_VALUES: set[RegistrarTLDPriceDetailRequestKind] = {
    "generic",
}


def check_registrar_tld_price_detail_request_kind(value: str) -> RegistrarTLDPriceDetailRequestKind:
    if value in REGISTRAR_TLD_PRICE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_DETAIL_REQUEST_KIND_VALUES!r}")
