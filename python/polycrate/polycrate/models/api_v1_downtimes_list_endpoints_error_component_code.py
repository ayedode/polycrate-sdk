from typing import Literal

ApiV1DowntimesListEndpointsErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_DOWNTIMES_LIST_ENDPOINTS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1DowntimesListEndpointsErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_downtimes_list_endpoints_error_component_code(
    value: str,
) -> ApiV1DowntimesListEndpointsErrorComponentCode:
    if value in API_V1_DOWNTIMES_LIST_ENDPOINTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_ENDPOINTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
