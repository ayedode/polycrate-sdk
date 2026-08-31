from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_criticality_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateCriticalityErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
