from typing import Literal

ApiV1RegistryRegistriesCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_REGISTRY_REGISTRIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_registry_registries_create_kind_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesCreateKindErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
