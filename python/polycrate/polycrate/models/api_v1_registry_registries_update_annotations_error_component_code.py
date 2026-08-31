from typing import Literal

ApiV1RegistryRegistriesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_REGISTRY_REGISTRIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_registry_registries_update_annotations_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
