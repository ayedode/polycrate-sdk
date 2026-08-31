from typing import Literal

ApiV1RegistryRegistriesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_REGISTRY_REGISTRIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_registry_registries_update_annotations_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
