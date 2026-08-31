from typing import Literal

ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponentAttr = Literal["endpoint_monitors"]

API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponentAttr
] = {
    "endpoint_monitors",
}


def check_api_v1_workspaces_update_secrets_poly_partial_update_endpoint_monitors_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateSecretsPolyPartialUpdateEndpointMonitorsErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SECRETS_POLY_PARTIAL_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
