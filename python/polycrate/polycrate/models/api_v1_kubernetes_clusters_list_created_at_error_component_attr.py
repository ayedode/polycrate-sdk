from typing import Literal

ApiV1KubernetesClustersListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_KUBERNETES_CLUSTERS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_kubernetes_clusters_list_created_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersListCreatedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
