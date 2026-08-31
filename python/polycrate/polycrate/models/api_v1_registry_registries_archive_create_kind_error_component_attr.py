from typing import Literal

ApiV1RegistryRegistriesArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_registry_registries_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateKindErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
