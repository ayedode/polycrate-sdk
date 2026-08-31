from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponentAttr = Literal["storage_class"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponentAttr
] = {
    "storage_class",
}


def check_api_v1_kubernetes_controlplanes_partial_update_storage_class_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
