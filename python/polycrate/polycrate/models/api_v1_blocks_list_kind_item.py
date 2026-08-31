from typing import Literal

ApiV1BlocksListKindItem = Literal[
    "dockerapp", "generic", "k8sapp", "k8sappinstance", "k8scluster", "library", "linuxapp"
]

API_V1_BLOCKS_LIST_KIND_ITEM_VALUES: set[ApiV1BlocksListKindItem] = {
    "dockerapp",
    "generic",
    "k8sapp",
    "k8sappinstance",
    "k8scluster",
    "library",
    "linuxapp",
}


def check_api_v1_blocks_list_kind_item(value: str) -> ApiV1BlocksListKindItem:
    if value in API_V1_BLOCKS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LIST_KIND_ITEM_VALUES!r}")
