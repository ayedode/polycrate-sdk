from typing import Literal

ApiV1DowntimesListKindItem = Literal[
    "customer-caused",
    "emergency-maintenance",
    "false-positive",
    "force-majeure",
    "generic",
    "planned-maintenance",
    "upstream-provider",
]

API_V1_DOWNTIMES_LIST_KIND_ITEM_VALUES: set[ApiV1DowntimesListKindItem] = {
    "customer-caused",
    "emergency-maintenance",
    "false-positive",
    "force-majeure",
    "generic",
    "planned-maintenance",
    "upstream-provider",
}


def check_api_v1_downtimes_list_kind_item(value: str) -> ApiV1DowntimesListKindItem:
    if value in API_V1_DOWNTIMES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_KIND_ITEM_VALUES!r}")
