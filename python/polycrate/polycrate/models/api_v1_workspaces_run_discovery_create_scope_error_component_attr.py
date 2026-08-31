from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_workspaces_run_discovery_create_scope_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateScopeErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
