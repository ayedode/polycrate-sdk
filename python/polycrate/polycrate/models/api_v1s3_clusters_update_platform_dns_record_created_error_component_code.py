from typing import Literal

ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponentCode = Literal["invalid", "null"]

API_V1S3_CLUSTERS_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_clusters_update_platform_dns_record_created_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdatePlatformDnsRecordCreatedErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
