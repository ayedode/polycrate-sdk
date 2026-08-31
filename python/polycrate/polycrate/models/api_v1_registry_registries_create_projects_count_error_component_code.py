from typing import Literal

ApiV1RegistryRegistriesCreateProjectsCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_REGISTRY_REGISTRIES_CREATE_PROJECTS_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesCreateProjectsCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_registry_registries_create_projects_count_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesCreateProjectsCountErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_PROJECTS_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_PROJECTS_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
