from typing import Literal

ApiV1RegionsListKindErrorComponentCode = Literal["invalid_choice", "invalid_list"]

API_V1_REGIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1RegionsListKindErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
}


def check_api_v1_regions_list_kind_error_component_code(value: str) -> ApiV1RegionsListKindErrorComponentCode:
    if value in API_V1_REGIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
