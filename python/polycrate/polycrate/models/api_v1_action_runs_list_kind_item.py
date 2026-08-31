from typing import Literal

ApiV1ActionRunsListKindItem = Literal["generic"]

API_V1_ACTION_RUNS_LIST_KIND_ITEM_VALUES: set[ApiV1ActionRunsListKindItem] = {
    "generic",
}


def check_api_v1_action_runs_list_kind_item(value: str) -> ApiV1ActionRunsListKindItem:
    if value in API_V1_ACTION_RUNS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_KIND_ITEM_VALUES!r}")
