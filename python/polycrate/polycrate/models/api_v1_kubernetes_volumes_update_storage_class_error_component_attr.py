from typing import Literal

ApiV1KubernetesVolumesUpdateStorageClassErrorComponentAttr = Literal["storage_class"]

API_V1_KUBERNETES_VOLUMES_UPDATE_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateStorageClassErrorComponentAttr
] = {
    "storage_class",
}


def check_api_v1_kubernetes_volumes_update_storage_class_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateStorageClassErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
