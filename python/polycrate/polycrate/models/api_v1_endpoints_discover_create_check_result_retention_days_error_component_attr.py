from typing import Literal

ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponentAttr = Literal["check_result_retention_days"]

API_V1_ENDPOINTS_DISCOVER_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponentAttr
] = {
    "check_result_retention_days",
}


def check_api_v1_endpoints_discover_create_check_result_retention_days_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateCheckResultRetentionDaysErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
