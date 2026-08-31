from typing import Literal

ApiV1KubernetesClustersListNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_CLUSTERS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_clusters_list_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersListNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
