from typing import Literal

ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponentAttr = Literal["dnssec_algorithm"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponentAttr
] = {
    "dnssec_algorithm",
}


def check_api_v1_domains_dnszones_archive_create_dnssec_algorithm_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateDnssecAlgorithmErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DNSSEC_ALGORITHM_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
