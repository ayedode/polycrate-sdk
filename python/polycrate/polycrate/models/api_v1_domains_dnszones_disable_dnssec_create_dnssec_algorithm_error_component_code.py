from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_dnssec_algorithm_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateDnssecAlgorithmErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
