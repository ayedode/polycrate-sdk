from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponentAttr = Literal["credential_id"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponentAttr
] = {
    "credential_id",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_credential_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateCredentialIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
