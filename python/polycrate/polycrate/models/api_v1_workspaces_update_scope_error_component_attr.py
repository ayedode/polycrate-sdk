from typing import Literal

ApiV1WorkspacesUpdateScopeErrorComponentAttr = Literal["scope"]

API_V1_WORKSPACES_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1WorkspacesUpdateScopeErrorComponentAttr] = {
    "scope",
}


def check_api_v1_workspaces_update_scope_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateScopeErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
