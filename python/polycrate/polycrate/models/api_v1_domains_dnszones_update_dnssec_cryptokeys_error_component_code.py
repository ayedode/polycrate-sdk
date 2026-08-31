from typing import Literal

ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_update_dnssec_cryptokeys_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesUpdateDnssecCryptokeysErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
