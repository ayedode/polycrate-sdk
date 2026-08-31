from typing import Literal

ApiV1RegistryRegistriesCreateNameErrorComponentAttr = Literal["name"]

API_V1_REGISTRY_REGISTRIES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_registry_registries_create_name_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateNameErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
