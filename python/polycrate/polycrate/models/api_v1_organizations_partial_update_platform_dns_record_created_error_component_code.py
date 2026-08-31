from typing import Literal

ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponentCode = Literal["invalid", "null"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_organizations_partial_update_platform_dns_record_created_error_component_code(
    value: str,
) -> ApiV1OrganizationsPartialUpdatePlatformDnsRecordCreatedErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
