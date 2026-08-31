from typing import Literal

ApiV1S3ClustersCreateCredentialErrorComponentAttr = Literal["credential"]

API_V1S3_CLUSTERS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateCredentialErrorComponentAttr
] = {
    "credential",
}


def check_api_v1s3_clusters_create_credential_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateCredentialErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_CREDENTIAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
