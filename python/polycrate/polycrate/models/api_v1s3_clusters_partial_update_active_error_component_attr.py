from typing import Literal

ApiV1S3ClustersPartialUpdateActiveErrorComponentAttr = Literal["active"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1s3_clusters_partial_update_active_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateActiveErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
