from typing import Literal

ApiV1ProjectsListSearchErrorComponentAttr = Literal["search"]

API_V1_PROJECTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_projects_list_search_error_component_attr(value: str) -> ApiV1ProjectsListSearchErrorComponentAttr:
    if value in API_V1_PROJECTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
