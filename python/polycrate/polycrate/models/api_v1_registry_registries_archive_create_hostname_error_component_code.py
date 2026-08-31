from typing import Literal

ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_registry_registries_archive_create_hostname_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateHostnameErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_HOSTNAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
