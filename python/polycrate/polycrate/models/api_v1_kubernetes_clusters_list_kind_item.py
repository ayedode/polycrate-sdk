from typing import Literal

ApiV1KubernetesClustersListKindItem = Literal["generic", "loopback", "polycrate"]

API_V1_KUBERNETES_CLUSTERS_LIST_KIND_ITEM_VALUES: set[ApiV1KubernetesClustersListKindItem] = {
    "generic",
    "loopback",
    "polycrate",
}


def check_api_v1_kubernetes_clusters_list_kind_item(value: str) -> ApiV1KubernetesClustersListKindItem:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_KIND_ITEM_VALUES!r}")
