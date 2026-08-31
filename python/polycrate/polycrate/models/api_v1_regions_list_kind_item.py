from typing import Literal

ApiV1RegionsListKindItem = Literal["generic"]

API_V1_REGIONS_LIST_KIND_ITEM_VALUES: set[ApiV1RegionsListKindItem] = {
    "generic",
}


def check_api_v1_regions_list_kind_item(value: str) -> ApiV1RegionsListKindItem:
    if value in API_V1_REGIONS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_LIST_KIND_ITEM_VALUES!r}")
