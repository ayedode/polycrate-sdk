from typing import Literal

ApiV1KubernetesClustersUpdateActiveErrorComponentAttr = Literal["active"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_kubernetes_clusters_update_active_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersUpdateActiveErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
