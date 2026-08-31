from typing import Literal

ApiV1AlertroutersListKindItem = Literal["dummy", "generic"]

API_V1_ALERTROUTERS_LIST_KIND_ITEM_VALUES: set[ApiV1AlertroutersListKindItem] = {
    "dummy",
    "generic",
}


def check_api_v1_alertrouters_list_kind_item(value: str) -> ApiV1AlertroutersListKindItem:
    if value in API_V1_ALERTROUTERS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_LIST_KIND_ITEM_VALUES!r}")
