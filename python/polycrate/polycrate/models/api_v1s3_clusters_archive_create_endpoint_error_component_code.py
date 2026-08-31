from typing import Literal

ApiV1S3ClustersArchiveCreateEndpointErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_ENDPOINT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersArchiveCreateEndpointErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1s3_clusters_archive_create_endpoint_error_component_code(
    value: str,
) -> ApiV1S3ClustersArchiveCreateEndpointErrorComponentCode:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_ENDPOINT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_ENDPOINT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
