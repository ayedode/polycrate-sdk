from typing import Literal

ApiV1DomainsRegistrarTldPricesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_STATE_VALUES: set[ApiV1DomainsRegistrarTldPricesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_domains_registrar_tld_prices_list_state(value: str) -> ApiV1DomainsRegistrarTldPricesListState:
    if value in API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_STATE_VALUES!r}"
    )
