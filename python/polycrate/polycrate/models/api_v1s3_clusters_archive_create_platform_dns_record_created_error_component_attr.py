from typing import Literal

ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponentAttr = Literal["platform_dns_record_created"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponentAttr
] = {
    "platform_dns_record_created",
}


def check_api_v1s3_clusters_archive_create_platform_dns_record_created_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreatePlatformDnsRecordCreatedErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
