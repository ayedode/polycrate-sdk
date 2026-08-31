from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateNameErrorComponentAttr = Literal["name"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_workspaces_run_discovery_create_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
