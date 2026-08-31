from typing import Literal

ApiV1RegistryRegistriesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_registry_registries_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
