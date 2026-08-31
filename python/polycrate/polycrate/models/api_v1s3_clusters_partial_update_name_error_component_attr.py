from typing import Literal

ApiV1S3ClustersPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1s3_clusters_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateNameErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
