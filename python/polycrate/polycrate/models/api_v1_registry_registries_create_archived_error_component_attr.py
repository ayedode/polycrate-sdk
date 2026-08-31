from typing import Literal

ApiV1RegistryRegistriesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_REGISTRY_REGISTRIES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_registry_registries_create_archived_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateArchivedErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
