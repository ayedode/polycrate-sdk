from typing import Literal

ApiV1CvesListKindItem = Literal["generic"]

API_V1_CVES_LIST_KIND_ITEM_VALUES: set[ApiV1CvesListKindItem] = {
    "generic",
}


def check_api_v1_cves_list_kind_item(value: str) -> ApiV1CvesListKindItem:
    if value in API_V1_CVES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_KIND_ITEM_VALUES!r}")
