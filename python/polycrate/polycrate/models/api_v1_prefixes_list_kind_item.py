from typing import Literal

ApiV1PrefixesListKindItem = Literal["ipv4", "ipv6"]

API_V1_PREFIXES_LIST_KIND_ITEM_VALUES: set[ApiV1PrefixesListKindItem] = {
    "ipv4",
    "ipv6",
}


def check_api_v1_prefixes_list_kind_item(value: str) -> ApiV1PrefixesListKindItem:
    if value in API_V1_PREFIXES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_LIST_KIND_ITEM_VALUES!r}")
