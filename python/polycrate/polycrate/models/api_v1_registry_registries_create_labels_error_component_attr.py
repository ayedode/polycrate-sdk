from typing import Literal

ApiV1RegistryRegistriesCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_REGISTRY_REGISTRIES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_registry_registries_create_labels_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesCreateLabelsErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
