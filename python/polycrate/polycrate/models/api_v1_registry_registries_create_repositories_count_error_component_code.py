from typing import Literal

ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_REGISTRY_REGISTRIES_CREATE_REPOSITORIES_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_registry_registries_create_repositories_count_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_REPOSITORIES_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_REPOSITORIES_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
