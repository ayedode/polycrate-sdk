from typing import Literal

ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponentAttr = Literal["pvc_namespace"]

API_V1_KUBERNETES_VOLUMES_UPDATE_PVC_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponentAttr
] = {
    "pvc_namespace",
}


def check_api_v1_kubernetes_volumes_update_pvc_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdatePvcNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_PVC_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_PVC_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
