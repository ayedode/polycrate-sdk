from typing import Literal

ApiV1EndpointsListKindItem = Literal["dns", "http", "icmp", "tcp"]

API_V1_ENDPOINTS_LIST_KIND_ITEM_VALUES: set[ApiV1EndpointsListKindItem] = {
    "dns",
    "http",
    "icmp",
    "tcp",
}


def check_api_v1_endpoints_list_kind_item(value: str) -> ApiV1EndpointsListKindItem:
    if value in API_V1_ENDPOINTS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_KIND_ITEM_VALUES!r}")
