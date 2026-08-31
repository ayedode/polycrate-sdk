from typing import Literal

ApiV1KubernetesClustersListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_KUBERNETES_CLUSTERS_LIST_STATE_VALUES: set[ApiV1KubernetesClustersListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_kubernetes_clusters_list_state(value: str) -> ApiV1KubernetesClustersListState:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_STATE_VALUES!r}")
