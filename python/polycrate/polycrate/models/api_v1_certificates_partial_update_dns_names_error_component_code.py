from typing import Literal

ApiV1CertificatesPartialUpdateDnsNamesErrorComponentCode = Literal["invalid", "null"]

API_V1_CERTIFICATES_PARTIAL_UPDATE_DNS_NAMES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesPartialUpdateDnsNamesErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_certificates_partial_update_dns_names_error_component_code(
    value: str,
) -> ApiV1CertificatesPartialUpdateDnsNamesErrorComponentCode:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_DNS_NAMES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_DNS_NAMES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
