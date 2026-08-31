from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_archived_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateArchivedErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
