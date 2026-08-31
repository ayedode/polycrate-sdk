from typing import Literal

ApiV1KubernetesClustersListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_CLUSTERS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesClustersListUpdatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_clusters_list_updated_at_error_component_code(
    value: str,
) -> ApiV1KubernetesClustersListUpdatedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
