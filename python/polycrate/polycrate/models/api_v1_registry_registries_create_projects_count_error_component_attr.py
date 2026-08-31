from typing import Literal

ApiV1RegistryRegistriesCreateProjectsCountErrorComponentAttr = Literal["projects_count"]

API_V1_REGISTRY_REGISTRIES_CREATE_PROJECTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateProjectsCountErrorComponentAttr
] = {
    "projects_count",
}


def check_api_v1_registry_registries_create_projects_count_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateProjectsCountErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_PROJECTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_PROJECTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
