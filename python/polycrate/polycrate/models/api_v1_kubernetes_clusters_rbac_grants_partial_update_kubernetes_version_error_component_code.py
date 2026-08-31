from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_KUBERNETES_VERSION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_kubernetes_version_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateKubernetesVersionErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_KUBERNETES_VERSION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_KUBERNETES_VERSION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
