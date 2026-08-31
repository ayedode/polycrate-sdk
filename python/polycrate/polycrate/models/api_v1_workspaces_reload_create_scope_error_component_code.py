from typing import Literal

ApiV1WorkspacesReloadCreateScopeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReloadCreateScopeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_reload_create_scope_error_component_code(
    value: str,
) -> ApiV1WorkspacesReloadCreateScopeErrorComponentCode:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
