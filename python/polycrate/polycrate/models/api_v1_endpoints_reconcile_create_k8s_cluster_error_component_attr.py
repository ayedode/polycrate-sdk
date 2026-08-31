from typing import Literal

ApiV1EndpointsReconcileCreateK8SClusterErrorComponentAttr = Literal["k8s_cluster"]

API_V1_ENDPOINTS_RECONCILE_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateK8SClusterErrorComponentAttr
] = {
    "k8s_cluster",
}


def check_api_v1_endpoints_reconcile_create_k8s_cluster_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateK8SClusterErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
