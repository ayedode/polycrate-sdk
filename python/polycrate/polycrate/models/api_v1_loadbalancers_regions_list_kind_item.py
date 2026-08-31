from typing import Literal

ApiV1LoadbalancersRegionsListKindItem = Literal["cilium", "metallb"]

API_V1_LOADBALANCERS_REGIONS_LIST_KIND_ITEM_VALUES: set[ApiV1LoadbalancersRegionsListKindItem] = {
    "cilium",
    "metallb",
}


def check_api_v1_loadbalancers_regions_list_kind_item(value: str) -> ApiV1LoadbalancersRegionsListKindItem:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_KIND_ITEM_VALUES!r}"
    )
