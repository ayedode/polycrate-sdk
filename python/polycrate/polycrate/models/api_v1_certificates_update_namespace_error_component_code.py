from typing import Literal

ApiV1CertificatesUpdateNamespaceErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_CERTIFICATES_UPDATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateNamespaceErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_certificates_update_namespace_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateNamespaceErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
