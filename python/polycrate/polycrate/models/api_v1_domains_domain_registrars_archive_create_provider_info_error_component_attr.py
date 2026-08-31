from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponentAttr = Literal["provider_info"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_PROVIDER_INFO_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponentAttr
] = {
    "provider_info",
}


def check_api_v1_domains_domain_registrars_archive_create_provider_info_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateProviderInfoErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_PROVIDER_INFO_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_PROVIDER_INFO_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
