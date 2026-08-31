from typing import Literal

ApiV1AlertsDiscoverCreateK8SClusterErrorComponentAttr = Literal["k8s_cluster"]

API_V1_ALERTS_DISCOVER_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsDiscoverCreateK8SClusterErrorComponentAttr
] = {
    "k8s_cluster",
}


def check_api_v1_alerts_discover_create_k8s_cluster_error_component_attr(
    value: str,
) -> ApiV1AlertsDiscoverCreateK8SClusterErrorComponentAttr:
    if value in API_V1_ALERTS_DISCOVER_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_DISCOVER_CREATE_K8S_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
