from typing import Literal

ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_PROJECTS_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_registry_registries_partial_update_projects_count_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateProjectsCountErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_PROJECTS_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_PROJECTS_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
