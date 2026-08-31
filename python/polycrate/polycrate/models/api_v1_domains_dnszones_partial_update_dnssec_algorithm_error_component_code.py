from typing import Literal

ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_dnszones_partial_update_dnssec_algorithm_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateDnssecAlgorithmErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_CODE_VALUES!r}"
    )
