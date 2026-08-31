from typing import Literal

ApiV1WorkspacesListKindItem = Literal["generic", "polycrate"]

API_V1_WORKSPACES_LIST_KIND_ITEM_VALUES: set[ApiV1WorkspacesListKindItem] = {
    "generic",
    "polycrate",
}


def check_api_v1_workspaces_list_kind_item(value: str) -> ApiV1WorkspacesListKindItem:
    if value in API_V1_WORKSPACES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LIST_KIND_ITEM_VALUES!r}")
