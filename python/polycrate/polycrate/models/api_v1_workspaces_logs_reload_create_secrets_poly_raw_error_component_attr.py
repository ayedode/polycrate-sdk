from typing import Literal

ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponentAttr = Literal["secrets_poly_raw"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_SECRETS_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponentAttr
] = {
    "secrets_poly_raw",
}


def check_api_v1_workspaces_logs_reload_create_secrets_poly_raw_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateSecretsPolyRawErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_SECRETS_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_SECRETS_POLY_RAW_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
