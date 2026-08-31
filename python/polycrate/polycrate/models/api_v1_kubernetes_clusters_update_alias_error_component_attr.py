from typing import Literal

ApiV1KubernetesClustersUpdateAliasErrorComponentAttr = Literal["alias"]

API_V1_KUBERNETES_CLUSTERS_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersUpdateAliasErrorComponentAttr
] = {
    "alias",
}


def check_api_v1_kubernetes_clusters_update_alias_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersUpdateAliasErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_UPDATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
