from typing import Literal

ApiV1S3ClustersUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1S3_CLUSTERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1s3_clusters_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
