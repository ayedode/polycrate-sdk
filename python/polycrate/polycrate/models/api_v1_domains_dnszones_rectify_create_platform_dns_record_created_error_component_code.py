from typing import Literal

ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_rectify_create_platform_dns_record_created_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreatePlatformDnsRecordCreatedErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_PLATFORM_DNS_RECORD_CREATED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
