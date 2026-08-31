from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateModifiedByUserErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
