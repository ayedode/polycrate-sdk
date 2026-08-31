from typing import Literal

ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponentAttr = Literal["operator_loglevel"]

API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponentAttr
] = {
    "operator_loglevel",
}


def check_api_v1_kubernetes_clusters_rbac_grants_create_operator_loglevel_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersRbacGrantsCreateOperatorLoglevelErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_RBAC_GRANTS_CREATE_OPERATOR_LOGLEVEL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
