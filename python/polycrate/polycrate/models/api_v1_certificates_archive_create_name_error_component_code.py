from typing import Literal

ApiV1CertificatesArchiveCreateNameErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "min_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_CERTIFICATES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CertificatesArchiveCreateNameErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "min_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_certificates_archive_create_name_error_component_code(
    value: str,
) -> ApiV1CertificatesArchiveCreateNameErrorComponentCode:
    if value in API_V1_CERTIFICATES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CERTIFICATES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
