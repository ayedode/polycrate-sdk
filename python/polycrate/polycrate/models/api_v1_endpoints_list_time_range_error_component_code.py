from typing import Literal

ApiV1EndpointsListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_ENDPOINTS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1EndpointsListTimeRangeErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_endpoints_list_time_range_error_component_code(
    value: str,
) -> ApiV1EndpointsListTimeRangeErrorComponentCode:
    if value in API_V1_ENDPOINTS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
