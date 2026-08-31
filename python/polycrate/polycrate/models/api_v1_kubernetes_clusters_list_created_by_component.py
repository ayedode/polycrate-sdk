from typing import Literal

ApiV1KubernetesClustersListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_KUBERNETES_CLUSTERS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1KubernetesClustersListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_kubernetes_clusters_list_created_by_component(
    value: str,
) -> ApiV1KubernetesClustersListCreatedByComponent:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
