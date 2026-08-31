from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponentAttr = Literal["kind"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_kind_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateKindErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
