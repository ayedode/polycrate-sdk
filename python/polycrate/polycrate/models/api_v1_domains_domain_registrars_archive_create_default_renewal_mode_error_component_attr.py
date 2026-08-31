from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponentAttr = Literal["default_renewal_mode"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponentAttr
] = {
    "default_renewal_mode",
}


def check_api_v1_domains_domain_registrars_archive_create_default_renewal_mode_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateDefaultRenewalModeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
