from typing import Literal

ApiV1RegistryRegistriesListWorkspacesErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_REGISTRY_REGISTRIES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesListWorkspacesErrorComponentCode
] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_registry_registries_list_workspaces_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesListWorkspacesErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_LIST_WORKSPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
