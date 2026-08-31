from typing import Literal

ApiV1CertificatesUpdateDnsNamesErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_UPDATE_DNS_NAMES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateDnsNamesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_update_dns_names_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateDnsNamesErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_DNS_NAMES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_DNS_NAMES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
