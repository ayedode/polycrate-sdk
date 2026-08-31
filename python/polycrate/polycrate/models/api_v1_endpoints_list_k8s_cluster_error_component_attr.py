from typing import Literal

ApiV1EndpointsListK8SClusterErrorComponentAttr = Literal["k8s_cluster"]

API_V1_ENDPOINTS_LIST_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1EndpointsListK8SClusterErrorComponentAttr] = {
    "k8s_cluster",
}


def check_api_v1_endpoints_list_k8s_cluster_error_component_attr(
    value: str,
) -> ApiV1EndpointsListK8SClusterErrorComponentAttr:
    if value in API_V1_ENDPOINTS_LIST_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
