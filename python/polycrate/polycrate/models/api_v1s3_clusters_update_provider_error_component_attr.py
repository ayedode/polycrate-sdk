from typing import Literal

ApiV1S3ClustersUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1S3_CLUSTERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3ClustersUpdateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1s3_clusters_update_provider_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateProviderErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
