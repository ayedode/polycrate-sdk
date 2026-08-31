from typing import Literal

ApiV1CredentialsListS3ClustersErrorComponentAttr = Literal["s3_clusters"]

API_V1_CREDENTIALS_LIST_S3_CLUSTERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsListS3ClustersErrorComponentAttr
] = {
    "s3_clusters",
}


def check_api_v1_credentials_list_s3_clusters_error_component_attr(
    value: str,
) -> ApiV1CredentialsListS3ClustersErrorComponentAttr:
    if value in API_V1_CREDENTIALS_LIST_S3_CLUSTERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_S3_CLUSTERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
