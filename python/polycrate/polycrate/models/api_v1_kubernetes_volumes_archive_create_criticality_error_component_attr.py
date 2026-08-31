from typing import Literal

ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_volumes_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
