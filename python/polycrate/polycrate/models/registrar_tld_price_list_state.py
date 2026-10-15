from typing import Literal

RegistrarTLDPriceListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

REGISTRAR_TLD_PRICE_LIST_STATE_VALUES: set[RegistrarTLDPriceListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_registrar_tld_price_list_state(value: str) -> RegistrarTLDPriceListState:
    if value in REGISTRAR_TLD_PRICE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGISTRAR_TLD_PRICE_LIST_STATE_VALUES!r}")
