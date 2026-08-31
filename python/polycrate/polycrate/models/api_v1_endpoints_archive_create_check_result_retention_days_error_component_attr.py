from typing import Literal

ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponentAttr = Literal["check_result_retention_days"]

API_V1_ENDPOINTS_ARCHIVE_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponentAttr
] = {
    "check_result_retention_days",
}


def check_api_v1_endpoints_archive_create_check_result_retention_days_error_component_attr(
    value: str,
) -> ApiV1EndpointsArchiveCreateCheckResultRetentionDaysErrorComponentAttr:
    if value in API_V1_ENDPOINTS_ARCHIVE_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_ARCHIVE_CREATE_CHECK_RESULT_RETENTION_DAYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
