from typing import Literal

ApiV1DowntimesListKubernetesClustersErrorComponentAttr = Literal["kubernetes_clusters"]

API_V1_DOWNTIMES_LIST_KUBERNETES_CLUSTERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesListKubernetesClustersErrorComponentAttr
] = {
    "kubernetes_clusters",
}


def check_api_v1_downtimes_list_kubernetes_clusters_error_component_attr(
    value: str,
) -> ApiV1DowntimesListKubernetesClustersErrorComponentAttr:
    if value in API_V1_DOWNTIMES_LIST_KUBERNETES_CLUSTERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_LIST_KUBERNETES_CLUSTERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
