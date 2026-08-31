from typing import Literal

ApiV1ContactgroupsListKindItem = Literal["dynamic", "generic"]

API_V1_CONTACTGROUPS_LIST_KIND_ITEM_VALUES: set[ApiV1ContactgroupsListKindItem] = {
    "dynamic",
    "generic",
}


def check_api_v1_contactgroups_list_kind_item(value: str) -> ApiV1ContactgroupsListKindItem:
    if value in API_V1_CONTACTGROUPS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_LIST_KIND_ITEM_VALUES!r}")
