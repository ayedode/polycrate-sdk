from typing import Literal

ApiV1KubernetesClustersCreateActiveErrorComponentAttr = Literal["active"]

API_V1_KUBERNETES_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_kubernetes_clusters_create_active_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersCreateActiveErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
