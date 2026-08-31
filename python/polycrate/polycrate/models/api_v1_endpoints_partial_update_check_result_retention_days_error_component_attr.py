from typing import Literal

ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponentAttr = Literal["check_result_retention_days"]

API_V1_ENDPOINTS_PARTIAL_UPDATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponentAttr
] = {
    "check_result_retention_days",
}


def check_api_v1_endpoints_partial_update_check_result_retention_days_error_component_attr(
    value: str,
) -> ApiV1EndpointsPartialUpdateCheckResultRetentionDaysErrorComponentAttr:
    if value in API_V1_ENDPOINTS_PARTIAL_UPDATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_PARTIAL_UPDATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
