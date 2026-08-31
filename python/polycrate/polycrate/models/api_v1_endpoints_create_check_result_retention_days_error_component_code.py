from typing import Literal

ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_ENDPOINTS_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_endpoints_create_check_result_retention_days_error_component_code(
    value: str,
) -> ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponentCode:
    if value in API_V1_ENDPOINTS_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
