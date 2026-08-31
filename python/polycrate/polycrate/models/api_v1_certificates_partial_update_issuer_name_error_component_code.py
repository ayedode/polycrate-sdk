from typing import Literal

ApiV1CertificatesPartialUpdateIssuerNameErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CERTIFICATES_PARTIAL_UPDATE_ISSUER_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesPartialUpdateIssuerNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_certificates_partial_update_issuer_name_error_component_code(
    value: str,
) -> ApiV1CertificatesPartialUpdateIssuerNameErrorComponentCode:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_ISSUER_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_ISSUER_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
