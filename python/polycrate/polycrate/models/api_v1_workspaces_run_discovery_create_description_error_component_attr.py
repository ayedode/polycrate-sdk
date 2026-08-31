from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_workspaces_run_discovery_create_description_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateDescriptionErrorComponentAttr:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
