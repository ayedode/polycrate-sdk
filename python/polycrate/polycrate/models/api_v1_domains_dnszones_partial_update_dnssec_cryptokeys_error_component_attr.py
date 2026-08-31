from typing import Literal

ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponentAttr = Literal["dnssec_cryptokeys"]

API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponentAttr
] = {
    "dnssec_cryptokeys",
}


def check_api_v1_domains_dnszones_partial_update_dnssec_cryptokeys_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesPartialUpdateDnssecCryptokeysErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_PARTIAL_UPDATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
