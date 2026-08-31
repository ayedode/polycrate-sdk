from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_annotations_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateAnnotationsErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
