from typing import Literal

ApiV1RegistryRegistriesUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_REGISTRY_REGISTRIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_registry_registries_update_labels_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesUpdateLabelsErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
