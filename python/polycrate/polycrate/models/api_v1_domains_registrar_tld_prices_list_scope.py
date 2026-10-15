from typing import Literal

ApiV1DomainsRegistrarTldPricesListScope = Literal["system", "user"]

API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_SCOPE_VALUES: set[ApiV1DomainsRegistrarTldPricesListScope] = {
    "system",
    "user",
}


def check_api_v1_domains_registrar_tld_prices_list_scope(value: str) -> ApiV1DomainsRegistrarTldPricesListScope:
    if value in API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_SCOPE_VALUES!r}"
    )
