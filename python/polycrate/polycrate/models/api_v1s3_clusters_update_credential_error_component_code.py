from typing import Literal

ApiV1S3ClustersUpdateCredentialErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1S3_CLUSTERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersUpdateCredentialErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1s3_clusters_update_credential_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdateCredentialErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_CREDENTIAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
