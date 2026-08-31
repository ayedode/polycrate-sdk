from typing import Literal

ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponentCode = Literal["invalid"]

API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_domains_dnszones_rectify_create_dnssec_cryptokeys_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesRectifyCreateDnssecCryptokeysErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_RECTIFY_CREATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
