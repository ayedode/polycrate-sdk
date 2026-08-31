from typing import Literal

ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponentAttr = Literal["operator_ignore_namespaces"]

API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_OPERATOR_IGNORE_NAMESPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponentAttr
] = {
    "operator_ignore_namespaces",
}


def check_api_v1_kubernetes_clusters_archive_create_operator_ignore_namespaces_error_component_attr(
    value: str,
) -> ApiV1KubernetesClustersArchiveCreateOperatorIgnoreNamespacesErrorComponentAttr:
    if value in API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_OPERATOR_IGNORE_NAMESPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CLUSTERS_ARCHIVE_CREATE_OPERATOR_IGNORE_NAMESPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
