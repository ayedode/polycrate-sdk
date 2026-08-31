from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_kind_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateKindErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
