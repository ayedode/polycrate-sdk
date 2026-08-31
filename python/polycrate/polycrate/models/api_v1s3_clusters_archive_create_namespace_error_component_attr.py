from typing import Literal

ApiV1S3ClustersArchiveCreateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1s3_clusters_archive_create_namespace_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateNamespaceErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
