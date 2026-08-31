from typing import Literal

ApiV1S3ClustersPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1s3_clusters_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
