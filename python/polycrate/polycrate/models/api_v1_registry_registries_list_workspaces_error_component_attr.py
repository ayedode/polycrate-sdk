from typing import Literal

ApiV1RegistryRegistriesListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_REGISTRY_REGISTRIES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_registry_registries_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesListWorkspacesErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
