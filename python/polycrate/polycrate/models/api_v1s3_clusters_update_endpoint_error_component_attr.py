from typing import Literal

ApiV1S3ClustersUpdateEndpointErrorComponentAttr = Literal["endpoint"]

API_V1S3_CLUSTERS_UPDATE_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersUpdateEndpointErrorComponentAttr] = {
    "endpoint",
}


def check_api_v1s3_clusters_update_endpoint_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateEndpointErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
