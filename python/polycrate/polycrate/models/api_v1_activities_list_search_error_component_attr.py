from typing import Literal

ApiV1ActivitiesListSearchErrorComponentAttr = Literal["search"]

API_V1_ACTIVITIES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActivitiesListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_activities_list_search_error_component_attr(value: str) -> ApiV1ActivitiesListSearchErrorComponentAttr:
    if value in API_V1_ACTIVITIES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTIVITIES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
