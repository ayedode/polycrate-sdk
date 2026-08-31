from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponentAttr = Literal[
    "global_endpoint_monitor"
]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponentAttr
] = {
    "global_endpoint_monitor",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_global_endpoint_monitor_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateGlobalEndpointMonitorErrorComponentAttr:
    if (
        value
        in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
