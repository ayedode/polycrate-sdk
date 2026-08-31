from typing import Literal

ApiV1CvesCreateCveIdErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
]

API_V1_CVES_CREATE_CVE_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesCreateCveIdErrorComponentCode] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_cves_create_cve_id_error_component_code(value: str) -> ApiV1CvesCreateCveIdErrorComponentCode:
    if value in API_V1_CVES_CREATE_CVE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_CVE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
