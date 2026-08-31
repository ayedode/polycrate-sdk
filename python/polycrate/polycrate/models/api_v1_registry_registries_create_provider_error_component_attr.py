from typing import Literal

ApiV1RegistryRegistriesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_REGISTRY_REGISTRIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_registry_registries_create_provider_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateProviderErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
