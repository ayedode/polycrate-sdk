from typing import Literal

ApiV1AgentsListKindItem = Literal["agent", "operator"]

API_V1_AGENTS_LIST_KIND_ITEM_VALUES: set[ApiV1AgentsListKindItem] = {
    "agent",
    "operator",
}


def check_api_v1_agents_list_kind_item(value: str) -> ApiV1AgentsListKindItem:
    if value in API_V1_AGENTS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_KIND_ITEM_VALUES!r}")
