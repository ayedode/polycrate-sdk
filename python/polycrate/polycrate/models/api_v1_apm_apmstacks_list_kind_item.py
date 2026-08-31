from typing import Literal

ApiV1ApmApmstacksListKindItem = Literal["generic"]

API_V1_APM_APMSTACKS_LIST_KIND_ITEM_VALUES: set[ApiV1ApmApmstacksListKindItem] = {
    "generic",
}


def check_api_v1_apm_apmstacks_list_kind_item(value: str) -> ApiV1ApmApmstacksListKindItem:
    if value in API_V1_APM_APMSTACKS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_APM_APMSTACKS_LIST_KIND_ITEM_VALUES!r}")
