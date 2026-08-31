from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateSloTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
