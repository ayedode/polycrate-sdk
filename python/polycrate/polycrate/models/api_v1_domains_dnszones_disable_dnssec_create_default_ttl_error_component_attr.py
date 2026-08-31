from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponentAttr = Literal["default_ttl"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DEFAULT_TTL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponentAttr
] = {
    "default_ttl",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_default_ttl_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateDefaultTtlErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DEFAULT_TTL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DEFAULT_TTL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
