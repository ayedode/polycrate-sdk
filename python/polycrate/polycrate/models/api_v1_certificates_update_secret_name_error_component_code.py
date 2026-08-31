from typing import Literal

ApiV1CertificatesUpdateSecretNameErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_CERTIFICATES_UPDATE_SECRET_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesUpdateSecretNameErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_certificates_update_secret_name_error_component_code(
    value: str,
) -> ApiV1CertificatesUpdateSecretNameErrorComponentCode:
    if value in API_V1_CERTIFICATES_UPDATE_SECRET_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_UPDATE_SECRET_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
