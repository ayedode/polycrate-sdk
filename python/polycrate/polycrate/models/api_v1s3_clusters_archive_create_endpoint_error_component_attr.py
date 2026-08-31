from typing import Literal

ApiV1S3ClustersArchiveCreateEndpointErrorComponentAttr = Literal["endpoint"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateEndpointErrorComponentAttr
] = {
    "endpoint",
}


def check_api_v1s3_clusters_archive_create_endpoint_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateEndpointErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
