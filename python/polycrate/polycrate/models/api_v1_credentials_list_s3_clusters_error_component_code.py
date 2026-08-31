from typing import Literal

ApiV1CredentialsListS3ClustersErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_CREDENTIALS_LIST_S3_CLUSTERS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsListS3ClustersErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_credentials_list_s3_clusters_error_component_code(
    value: str,
) -> ApiV1CredentialsListS3ClustersErrorComponentCode:
    if value in API_V1_CREDENTIALS_LIST_S3_CLUSTERS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_S3_CLUSTERS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
