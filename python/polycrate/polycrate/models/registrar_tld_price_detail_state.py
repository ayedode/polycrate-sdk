from typing import Literal

RegistrarTLDPriceDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

REGISTRAR_TLD_PRICE_DETAIL_STATE_VALUES: set[RegistrarTLDPriceDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_registrar_tld_price_detail_state(value: str) -> RegistrarTLDPriceDetailState:
    if value in REGISTRAR_TLD_PRICE_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_DETAIL_STATE_VALUES!r}")
