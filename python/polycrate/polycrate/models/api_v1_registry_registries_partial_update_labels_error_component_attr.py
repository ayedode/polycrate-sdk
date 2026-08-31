from typing import Literal

ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_registry_registries_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
