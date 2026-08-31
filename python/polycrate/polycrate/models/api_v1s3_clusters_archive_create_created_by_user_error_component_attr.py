from typing import Literal

ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponentAttr
] = {
    "created_by_user",
}


def check_api_v1s3_clusters_archive_create_created_by_user_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateCreatedByUserErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
