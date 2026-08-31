from typing import Literal

ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_organizations_reconcile_create_endpoint_monitoring_mode_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateEndpointMonitoringModeErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
