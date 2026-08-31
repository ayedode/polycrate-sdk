from typing import Literal

ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponentAttr = Literal["endpoint_monitoring_mode"]

API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponentAttr
] = {
    "endpoint_monitoring_mode",
}


def check_api_v1_organizations_archive_create_endpoint_monitoring_mode_error_component_attr(
    value: str,
) -> ApiV1OrganizationsArchiveCreateEndpointMonitoringModeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ARCHIVE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
