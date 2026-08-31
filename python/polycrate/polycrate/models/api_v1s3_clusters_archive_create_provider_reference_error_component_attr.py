from typing import Literal

ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1s3_clusters_archive_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateProviderReferenceErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
