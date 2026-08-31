from typing import Literal

ApiV1S3ClustersArchiveCreateAliasErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersArchiveCreateAliasErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1s3_clusters_archive_create_alias_error_component_code(
    value: str,
) -> ApiV1S3ClustersArchiveCreateAliasErrorComponentCode:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_ALIAS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
