from typing import Literal

ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_dnsrecords_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsArchiveCreateProviderErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
