from typing import Literal

ApiV1AlertroutersListSearchErrorComponentAttr = Literal["search"]

API_V1_ALERTROUTERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1AlertroutersListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_alertrouters_list_search_error_component_attr(
    value: str,
) -> ApiV1AlertroutersListSearchErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
