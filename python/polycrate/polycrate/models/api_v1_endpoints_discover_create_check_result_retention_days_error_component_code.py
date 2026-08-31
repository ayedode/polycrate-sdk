from typing import Literal

ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ENDPOINTS_DISCOVER_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_endpoints_discover_create_check_result_retention_days_error_component_code(
    value: str,
) -> ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponentCode:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
