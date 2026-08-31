from typing import Literal

ApiV1AgentsListSearchErrorComponentAttr = Literal["search"]

API_V1_AGENTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AgentsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_agents_list_search_error_component_attr(value: str) -> ApiV1AgentsListSearchErrorComponentAttr:
    if value in API_V1_AGENTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_AGENTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
