from typing import Literal

ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PVC_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_volumes_partial_update_pvc_namespace_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdatePvcNamespaceErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PVC_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PVC_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
