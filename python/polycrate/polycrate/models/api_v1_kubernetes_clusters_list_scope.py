from typing import Literal

ApiV1KubernetesClustersListScope = Literal["system", "user"]

API_V1_KUBERNETES_CLUSTERS_LIST_SCOPE_VALUES: set[ApiV1KubernetesClustersListScope] = {
    "system",
    "user",
}


def check_api_v1_kubernetes_clusters_list_scope(value: str) -> ApiV1KubernetesClustersListScope:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_SCOPE_VALUES!r}")
