from typing import Literal

ApiV1RegistryRegistriesUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_REGISTRY_REGISTRIES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_registry_registries_update_provider_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesUpdateProviderErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
