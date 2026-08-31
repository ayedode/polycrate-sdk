from typing import Literal

ApiV1S3ClustersCreateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1S3_CLUSTERS_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersCreateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1s3_clusters_create_credential_error_component_code(
    value: str,
) -> ApiV1S3ClustersCreateCredentialErrorComponentCode:
    if value in API_V1S3_CLUSTERS_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
