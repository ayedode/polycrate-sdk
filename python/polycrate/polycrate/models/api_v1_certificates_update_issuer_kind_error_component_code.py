from typing import Literal

ApiV1CertificatesUpdateIssuerKindErrorComponentCode = Literal["invalid_choice"]

API_V1_CERTIFICATES_UPDATE_ISSUER_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateIssuerKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_certificates_update_issuer_kind_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateIssuerKindErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_ISSUER_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_ISSUER_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
