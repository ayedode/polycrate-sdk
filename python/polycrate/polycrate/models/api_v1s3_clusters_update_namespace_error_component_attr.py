from typing import Literal

ApiV1S3ClustersUpdateNamespaceErrorComponentAttr = Literal["namespace"]

API_V1S3_CLUSTERS_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateNamespaceErrorComponentAttr
] = {
    "namespace",
}


def check_api_v1s3_clusters_update_namespace_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateNamespaceErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_NAMESPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
