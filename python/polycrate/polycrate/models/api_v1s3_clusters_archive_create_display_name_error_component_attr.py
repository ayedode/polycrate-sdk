from typing import Literal

ApiV1S3ClustersArchiveCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1s3_clusters_archive_create_display_name_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateDisplayNameErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
