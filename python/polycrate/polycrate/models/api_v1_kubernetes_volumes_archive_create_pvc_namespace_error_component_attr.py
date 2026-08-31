from typing import Literal

ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponentAttr = Literal["pvc_namespace"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PVC_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponentAttr
] = {
    "pvc_namespace",
}


def check_api_v1_kubernetes_volumes_archive_create_pvc_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreatePvcNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PVC_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PVC_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
