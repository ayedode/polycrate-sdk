from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponentAttr = Literal["name"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_name_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateNameErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
