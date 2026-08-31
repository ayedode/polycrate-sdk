from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_dnssec_cryptokeys_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateDnssecCryptokeysErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
