from typing import Literal

ApiV1IncidentsListSearchErrorComponentAttr = Literal["search"]

API_V1_INCIDENTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1IncidentsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_incidents_list_search_error_component_attr(value: str) -> ApiV1IncidentsListSearchErrorComponentAttr:
    if value in API_V1_INCIDENTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
