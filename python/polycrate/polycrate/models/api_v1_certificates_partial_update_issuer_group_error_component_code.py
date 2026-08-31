from typing import Literal

ApiV1CertificatesPartialUpdateIssuerGroupErrorComponentCode = Literal[
    "blank", "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CERTIFICATES_PARTIAL_UPDATE_ISSUER_GROUP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesPartialUpdateIssuerGroupErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_certificates_partial_update_issuer_group_error_component_code(
    value: str,
) -> ApiV1CertificatesPartialUpdateIssuerGroupErrorComponentCode:
    if value in API_V1_CERTIFICATES_PARTIAL_UPDATE_ISSUER_GROUP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_PARTIAL_UPDATE_ISSUER_GROUP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
