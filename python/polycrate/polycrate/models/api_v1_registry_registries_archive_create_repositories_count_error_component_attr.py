from typing import Literal

ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponentAttr = Literal["repositories_count"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_REPOSITORIES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponentAttr
] = {
    "repositories_count",
}


def check_api_v1_registry_registries_archive_create_repositories_count_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateRepositoriesCountErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_REPOSITORIES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_REPOSITORIES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
