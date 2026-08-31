from typing import Literal

ApiV1EndpointsCreateSloWindowDaysErrorComponentCode = Literal["invalid", "max_string_length", "max_value", "min_value"]

API_V1_ENDPOINTS_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsCreateSloWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_endpoints_create_slo_window_days_error_component_code(
    value: str,
) -> ApiV1EndpointsCreateSloWindowDaysErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
