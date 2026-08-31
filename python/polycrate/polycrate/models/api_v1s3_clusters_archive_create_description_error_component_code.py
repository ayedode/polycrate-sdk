from typing import Literal

ApiV1S3ClustersArchiveCreateDescriptionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersArchiveCreateDescriptionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1s3_clusters_archive_create_description_error_component_code(
    value: str,
) -> ApiV1S3ClustersArchiveCreateDescriptionErrorComponentCode:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
