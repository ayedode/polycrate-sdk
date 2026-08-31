from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateTolerationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
