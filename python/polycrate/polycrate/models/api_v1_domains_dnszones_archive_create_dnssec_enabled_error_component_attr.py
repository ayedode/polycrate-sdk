from typing import Literal

ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponentAttr = Literal["dnssec_enabled"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DNSSEC_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponentAttr
] = {
    "dnssec_enabled",
}


def check_api_v1_domains_dnszones_archive_create_dnssec_enabled_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateDnssecEnabledErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DNSSEC_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DNSSEC_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
