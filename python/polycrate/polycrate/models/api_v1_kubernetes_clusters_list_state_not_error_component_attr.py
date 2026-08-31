from typing import Literal

ApiV1KubernetesClustersListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_KUBERNETES_CLUSTERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_kubernetes_clusters_list_state_not_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersListStateNotErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
