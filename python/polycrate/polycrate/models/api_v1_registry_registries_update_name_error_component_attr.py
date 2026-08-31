from typing import Literal

ApiV1RegistryRegistriesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_REGISTRY_REGISTRIES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_registry_registries_update_name_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesUpdateNameErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
