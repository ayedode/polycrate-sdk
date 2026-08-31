from typing import Literal

ApiV1HostsListKindItem = Literal["bare_metal", "vm"]

API_V1_HOSTS_LIST_KIND_ITEM_VALUES: set[ApiV1HostsListKindItem] = {
    "bare_metal",
    "vm",
}


def check_api_v1_hosts_list_kind_item(value: str) -> ApiV1HostsListKindItem:
    if value in API_V1_HOSTS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_LIST_KIND_ITEM_VALUES!r}")
