from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_criticality_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateCriticalityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
