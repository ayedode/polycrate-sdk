from typing import Literal

ApiV1KubernetesClustersUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_clusters_update_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersUpdateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
