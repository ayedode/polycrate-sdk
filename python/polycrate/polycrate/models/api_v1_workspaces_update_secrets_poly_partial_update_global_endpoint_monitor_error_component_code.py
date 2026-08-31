from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_global_endpoint_monitor_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponentCode:
    if (
        value
        in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
