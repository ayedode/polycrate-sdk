from typing import Literal

ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponentAttr = Literal["repositories_count"]

API_V1_REGISTRY_REGISTRIES_CREATE_REPOSITORIES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponentAttr
] = {
    "repositories_count",
}


def check_api_v1_registry_registries_create_repositories_count_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateRepositoriesCountErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_REPOSITORIES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_REPOSITORIES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
