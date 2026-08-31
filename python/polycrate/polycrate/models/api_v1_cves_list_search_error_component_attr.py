from typing import Literal

ApiV1CvesListSearchErrorComponentAttr = Literal["search"]

API_V1_CVES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1_cves_list_search_error_component_attr(value: str) -> ApiV1CvesListSearchErrorComponentAttr:
    if value in API_V1_CVES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
