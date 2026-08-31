from typing import Literal

ApiV1CertificatesUpdateDnsNamesErrorComponentAttr = Literal["dns_names"]

API_V1_CERTIFICATES_UPDATE_DNS_NAMES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CertificatesUpdateDnsNamesErrorComponentAttr
] = {
    "dns_names",
}


def check_api_v1_certificates_update_dns_names_error_component_attr(
    value: str,
) -> ApiV1CertificatesUpdateDnsNamesErrorComponentAttr:
    if value in API_V1_CERTIFICATES_UPDATE_DNS_NAMES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_DNS_NAMES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
