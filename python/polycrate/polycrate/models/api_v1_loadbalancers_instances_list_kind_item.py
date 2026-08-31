from typing import Literal

ApiV1LoadbalancersInstancesListKindItem = Literal["generic"]

API_V1_LOADBALANCERS_INSTANCES_LIST_KIND_ITEM_VALUES: set[ApiV1LoadbalancersInstancesListKindItem] = {
    "generic",
}


def check_api_v1_loadbalancers_instances_list_kind_item(value: str) -> ApiV1LoadbalancersInstancesListKindItem:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_KIND_ITEM_VALUES!r}"
    )
