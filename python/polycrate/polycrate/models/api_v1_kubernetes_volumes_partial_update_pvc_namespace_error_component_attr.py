from typing import Literal

ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponentAttr = Literal["pvc_namespace"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PVC_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponentAttr
] = {
    "pvc_namespace",
}


def check_api_v1_kubernetes_volumes_partial_update_pvc_namespace_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PVC_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PVC_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
