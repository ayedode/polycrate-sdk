from typing import Literal

ApiV1EndpointsUpdateSloWindowDaysErrorComponentCode = Literal["invalid", "max_string_length", "max_value", "min_value"]

API_V1_ENDPOINTS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsUpdateSloWindowDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_endpoints_update_slo_window_days_error_component_code(
    value: str,
) -> ApiV1EndpointsUpdateSloWindowDaysErrorComponentCode:
    if value in API_V1_ENDPOINTS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_UPDATE_SLO_WINDOW_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
