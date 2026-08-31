from typing import Literal

ApiV1S3ClustersCreateDescriptionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1S3_CLUSTERS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersCreateDescriptionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1s3_clusters_create_description_error_component_code(
    value: str,
) -> ApiV1S3ClustersCreateDescriptionErrorComponentCode:
    if value in API_V1S3_CLUSTERS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
