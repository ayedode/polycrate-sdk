from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_annotations_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateAnnotationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
