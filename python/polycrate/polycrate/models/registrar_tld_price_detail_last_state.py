from typing import Literal

RegistrarTLDPriceDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

REGISTRAR_TLD_PRICE_DETAIL_LAST_STATE_VALUES: set[RegistrarTLDPriceDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_registrar_tld_price_detail_last_state(value: str) -> RegistrarTLDPriceDetailLastState:
    if value in REGISTRAR_TLD_PRICE_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_DETAIL_LAST_STATE_VALUES!r}")
