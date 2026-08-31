from typing import Literal

ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponentAttr = Literal["dnssec_algorithm"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponentAttr
] = {
    "dnssec_algorithm",
}


def check_api_v1_domains_dnszones_rectify_create_dnssec_algorithm_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateDnssecAlgorithmErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
