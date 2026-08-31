from typing import Literal

ApiV1DomainsDnszonesEnableDnssecCreateAlgorithmErrorComponentAttr = Literal["algorithm"]

API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_ALGORITHM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesEnableDnssecCreateAlgorithmErrorComponentAttr
] = {
    "algorithm",
}


def check_api_v1_domains_dnszones_enable_dnssec_create_algorithm_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesEnableDnssecCreateAlgorithmErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_ALGORITHM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ENABLE_DNSSEC_CREATE_ALGORITHM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
