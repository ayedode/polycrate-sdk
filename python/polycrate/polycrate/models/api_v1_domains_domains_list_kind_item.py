from typing import Literal

ApiV1DomainsDomainsListKindItem = Literal["generic"]

API_V1_DOMAINS_DOMAINS_LIST_KIND_ITEM_VALUES: set[ApiV1DomainsDomainsListKindItem] = {
    "generic",
}


def check_api_v1_domains_domains_list_kind_item(value: str) -> ApiV1DomainsDomainsListKindItem:
    if value in API_V1_DOMAINS_DOMAINS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_KIND_ITEM_VALUES!r}")
