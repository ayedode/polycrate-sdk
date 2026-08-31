from typing import Literal

ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value"
]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_BASEROW_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_kubernetes_clusters_rbac_grants_partial_update_baserow_id_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsPartialUpdateBaserowIdErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_BASEROW_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_PARTIAL_UPDATE_BASEROW_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
