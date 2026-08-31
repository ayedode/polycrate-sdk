from typing import Literal

ApiV1RegistryRegistriesCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_REGISTRY_REGISTRIES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_registry_registries_create_labels_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesCreateLabelsErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
