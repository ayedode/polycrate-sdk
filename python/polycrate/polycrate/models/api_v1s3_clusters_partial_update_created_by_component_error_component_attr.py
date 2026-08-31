from typing import Literal

ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1s3_clusters_partial_update_created_by_component_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateCreatedByComponentErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
