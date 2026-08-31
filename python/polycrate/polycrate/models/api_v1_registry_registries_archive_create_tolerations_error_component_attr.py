from typing import Literal

ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_registry_registries_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
