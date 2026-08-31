from typing import Literal

ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_organizations_archive_create_endpoint_monitoring_mode_error_component_code(
    value: str,
) -> ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
