from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_operator_loglevel_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
