from typing import Literal

ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_REGISTRY_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_registry_registries_partial_update_registry_version_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateRegistryVersionErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_REGISTRY_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_REGISTRY_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
