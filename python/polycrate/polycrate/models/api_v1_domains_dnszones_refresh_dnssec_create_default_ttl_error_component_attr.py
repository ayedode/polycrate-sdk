from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponentAttr = Literal["default_ttl"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DEFAULT_TTL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponentAttr
] = {
    "default_ttl",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_default_ttl_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateDefaultTtlErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DEFAULT_TTL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DEFAULT_TTL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
