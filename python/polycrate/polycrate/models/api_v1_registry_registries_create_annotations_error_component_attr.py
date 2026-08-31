from typing import Literal

ApiV1RegistryRegistriesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_REGISTRY_REGISTRIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_registry_registries_create_annotations_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
