from typing import Literal

ApiV1RegistryRegistriesCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_REGISTRY_REGISTRIES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_registry_registries_create_provider_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesCreateProviderErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
