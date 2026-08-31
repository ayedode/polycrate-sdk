from typing import Literal

ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_REGISTRY_REGISTRIES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_registry_registries_update_provider_reference_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesUpdateProviderReferenceErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
