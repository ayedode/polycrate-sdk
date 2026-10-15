from typing import Literal

ApiV1DomainsRegistrarTldPricesListKindItem = Literal["generic"]

API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_KIND_ITEM_VALUES: set[ApiV1DomainsRegistrarTldPricesListKindItem] = {
    "generic",
}


def check_api_v1_domains_registrar_tld_prices_list_kind_item(value: str) -> ApiV1DomainsRegistrarTldPricesListKindItem:
    if value in API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_REGISTRAR_TLD_PRICES_LIST_KIND_ITEM_VALUES!r}"
    )
