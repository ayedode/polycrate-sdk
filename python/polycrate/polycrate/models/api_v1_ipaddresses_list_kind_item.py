from typing import Literal

ApiV1IpaddressesListKindItem = Literal["ipv4", "ipv6"]

API_V1_IPADDRESSES_LIST_KIND_ITEM_VALUES: set[ApiV1IpaddressesListKindItem] = {
    "ipv4",
    "ipv6",
}


def check_api_v1_ipaddresses_list_kind_item(value: str) -> ApiV1IpaddressesListKindItem:
    if value in API_V1_IPADDRESSES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_LIST_KIND_ITEM_VALUES!r}")
