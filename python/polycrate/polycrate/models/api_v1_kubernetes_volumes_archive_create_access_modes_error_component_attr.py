from typing import Literal

ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponentAttr = Literal["access_modes"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_ACCESS_MODES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponentAttr
] = {
    "access_modes",
}


def check_api_v1_kubernetes_volumes_archive_create_access_modes_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreateAccessModesErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_ACCESS_MODES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_ACCESS_MODES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
