from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_labels_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateLabelsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
