from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
