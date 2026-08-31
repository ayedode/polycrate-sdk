from typing import Literal

ApiV1S3ClustersCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1S3_CLUSTERS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1s3_clusters_create_display_name_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateDisplayNameErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
