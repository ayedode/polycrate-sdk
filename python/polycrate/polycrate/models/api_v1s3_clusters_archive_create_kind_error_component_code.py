from typing import Literal

ApiV1S3ClustersArchiveCreateKindErrorComponentCode = Literal["invalid_choice", "null", "required"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersArchiveCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
    "required",
}


def check_api_v1s3_clusters_archive_create_kind_error_component_code(
    value: str,
) -> ApiV1S3ClustersArchiveCreateKindErrorComponentCode:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
