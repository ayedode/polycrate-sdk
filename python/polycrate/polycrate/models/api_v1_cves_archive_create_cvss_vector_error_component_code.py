from typing import Literal

ApiV1CvesArchiveCreateCvssVectorErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CVES_ARCHIVE_CREATE_CVSS_VECTOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CvesArchiveCreateCvssVectorErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_cves_archive_create_cvss_vector_error_component_code(
    value: str,
) -> ApiV1CvesArchiveCreateCvssVectorErrorComponentCode:
    if value in API_V1_CVES_ARCHIVE_CREATE_CVSS_VECTOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_CVSS_VECTOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
