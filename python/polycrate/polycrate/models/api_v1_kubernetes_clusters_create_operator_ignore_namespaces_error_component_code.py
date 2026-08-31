from typing import Literal

ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_CREATE_OPERATOR_IGNORE_NAMESPACES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_create_operator_ignore_namespaces_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersCreateOperatorIgnoreNamespacesErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_OPERATOR_IGNORE_NAMESPACES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_OPERATOR_IGNORE_NAMESPACES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
