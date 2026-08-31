from typing import Literal

ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponentCode = Literal["invalid_choice"]

API_V1_ORGANIZATIONS_CHOICES_LIST_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_organizations_choices_list_endpoint_monitoring_mode_error_component_code(
    value: str,
) -> ApiV1OrganizationsChoicesListEndpointMonitoringModeErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_CHOICES_LIST_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CHOICES_LIST_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
