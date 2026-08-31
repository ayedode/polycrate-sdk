from typing import Literal

ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponentAttr = Literal["dnssec_cryptokeys"]

API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponentAttr
] = {
    "dnssec_cryptokeys",
}


def check_api_v1_domains_dnszones_archive_create_dnssec_cryptokeys_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesArchiveCreateDnssecCryptokeysErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_ARCHIVE_CREATE_DNSSEC_CRYPTOKEYS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
