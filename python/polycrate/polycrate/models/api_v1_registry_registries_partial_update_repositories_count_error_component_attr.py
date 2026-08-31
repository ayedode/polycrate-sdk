from typing import Literal

ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponentAttr = Literal["repositories_count"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_REPOSITORIES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponentAttr
] = {
    "repositories_count",
}


def check_api_v1_registry_registries_partial_update_repositories_count_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateRepositoriesCountErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_REPOSITORIES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_REPOSITORIES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
