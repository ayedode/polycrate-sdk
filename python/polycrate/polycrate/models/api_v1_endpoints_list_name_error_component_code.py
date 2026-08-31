from typing import Literal

ApiV1EndpointsListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_ENDPOINTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1EndpointsListNameErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_endpoints_list_name_error_component_code(value: str) -> ApiV1EndpointsListNameErrorComponentCode:
    if value in API_V1_ENDPOINTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
