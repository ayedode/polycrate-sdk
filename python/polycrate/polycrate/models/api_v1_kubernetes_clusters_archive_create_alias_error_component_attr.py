from typing import Literal

ApiV1KubernetesClustersArchiveCreateAliasErrorComponentAttr = Literal["alias"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateAliasErrorComponentAttr
] = {
    "alias",
}


def check_api_v1_kubernetes_clusters_archive_create_alias_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateAliasErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
