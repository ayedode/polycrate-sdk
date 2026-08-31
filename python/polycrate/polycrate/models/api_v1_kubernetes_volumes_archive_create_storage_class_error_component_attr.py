from typing import Literal

ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponentAttr = Literal["storage_class"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponentAttr
] = {
    "storage_class",
}


def check_api_v1_kubernetes_volumes_archive_create_storage_class_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateStorageClassErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
