from typing import Literal

ApiV1CvesCreateCvssScoreErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_CVES_CREATE_CVSS_SCORE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesCreateCvssScoreErrorComponentCode] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_cves_create_cvss_score_error_component_code(value: str) -> ApiV1CvesCreateCvssScoreErrorComponentCode:
    if value in API_V1_CVES_CREATE_CVSS_SCORE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_CVSS_SCORE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
