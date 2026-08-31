from typing import Literal

ApiV1RegistryRegistriesUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_REGISTRY_REGISTRIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_registry_registries_update_archived_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesUpdateArchivedErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
