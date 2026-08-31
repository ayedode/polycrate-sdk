from typing import Literal

ApiV1DomainsDnsrecordsListKindItem = Literal["generic"]

API_V1_DOMAINS_DNSRECORDS_LIST_KIND_ITEM_VALUES: set[ApiV1DomainsDnsrecordsListKindItem] = {
    "generic",
}


def check_api_v1_domains_dnsrecords_list_kind_item(value: str) -> ApiV1DomainsDnsrecordsListKindItem:
    if value in API_V1_DOMAINS_DNSRECORDS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_LIST_KIND_ITEM_VALUES!r}")
