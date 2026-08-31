from typing import Literal

ApiV1S3ClustersUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1S3_CLUSTERS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3ClustersUpdateProviderErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1s3_clusters_update_provider_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdateProviderErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
