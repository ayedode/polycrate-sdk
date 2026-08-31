from typing import Literal

ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponentAttr = Literal["check_result_retention_days"]

API_V1_ENDPOINTS_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponentAttr
] = {
    "check_result_retention_days",
}


def check_api_v1_endpoints_create_check_result_retention_days_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateCheckResultRetentionDaysErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
