from typing import Literal

ApiV1CvesCreateCvssVectorErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_CVES_CREATE_CVSS_VECTOR_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesCreateCvssVectorErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_cves_create_cvss_vector_error_component_code(
    value: str,
) -> ApiV1CvesCreateCvssVectorErrorComponentCode:
    if value in API_V1_CVES_CREATE_CVSS_VECTOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_CVSS_VECTOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
