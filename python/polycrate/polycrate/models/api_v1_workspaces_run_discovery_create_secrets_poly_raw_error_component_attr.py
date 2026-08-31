from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponentAttr = Literal["secrets_poly_raw"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SECRETS_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponentAttr
] = {
    "secrets_poly_raw",
}


def check_api_v1_workspaces_run_discovery_create_secrets_poly_raw_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateSecretsPolyRawErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SECRETS_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SECRETS_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
