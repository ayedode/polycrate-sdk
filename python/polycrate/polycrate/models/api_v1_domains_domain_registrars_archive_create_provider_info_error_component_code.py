from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_PROVIDER_INFO_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_domain_registrars_archive_create_provider_info_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_PROVIDER_INFO_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_PROVIDER_INFO_ERROR_COMPONENT_CODE_VALUES!r}"
    )
