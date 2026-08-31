from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_run_discovery_create_scope_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
