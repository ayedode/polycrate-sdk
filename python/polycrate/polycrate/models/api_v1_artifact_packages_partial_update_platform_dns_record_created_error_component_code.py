from typing import Literal

ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponentCode = Literal["invalid", "null"]

API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_artifact_packages_partial_update_platform_dns_record_created_error_component_code(
    value: str,
) -> ApiV1ArtifactPackagesPartialUpdatePlatformDnsRecordCreatedErrorComponentCode:
    if value in API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACT_PACKAGES_PARTIAL_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
