from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
