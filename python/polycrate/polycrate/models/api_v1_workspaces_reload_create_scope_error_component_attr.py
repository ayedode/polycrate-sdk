from typing import Literal

ApiV1WorkspacesReloadCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_WORKSPACES_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_workspaces_reload_create_scope_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateScopeErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
