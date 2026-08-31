from typing import Literal

ApiV1WorkspacesCheckCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_WORKSPACES_CHECK_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_workspaces_check_create_scope_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateScopeErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
