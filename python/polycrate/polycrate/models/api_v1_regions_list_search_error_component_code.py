from typing import Literal

ApiV1RegionsListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_REGIONS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[ApiV1RegionsListSearchErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_regions_list_search_error_component_code(value: str) -> ApiV1RegionsListSearchErrorComponentCode:
    if value in API_V1_REGIONS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
