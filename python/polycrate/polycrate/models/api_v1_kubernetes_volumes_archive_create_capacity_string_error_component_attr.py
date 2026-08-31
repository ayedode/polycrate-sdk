from typing import Literal

ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponentAttr = Literal["capacity_string"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_CAPACITY_STRING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponentAttr
] = {
    "capacity_string",
}


def check_api_v1_kubernetes_volumes_archive_create_capacity_string_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateCapacityStringErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_CAPACITY_STRING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_CAPACITY_STRING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
