from typing import Literal

ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_organizations_icon_upload_create_endpoint_monitoring_mode_error_component_code(
    value: str,
) -> ApiV1OrganizationsIconUploadCreateEndpointMonitoringModeErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_ICON_UPLOAD_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
