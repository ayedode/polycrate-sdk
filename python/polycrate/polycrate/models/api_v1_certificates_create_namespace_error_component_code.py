from typing import Literal

ApiV1CertificatesCreateNamespaceErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_CERTIFICATES_CREATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesCreateNamespaceErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_certificates_create_namespace_error_component_code(
    value: str,
) -> ApiV1CertificatesCreateNamespaceErrorComponentCode:
    if value in API_V1_CERTIFICATES_CREATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_CREATE_NAMESPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
