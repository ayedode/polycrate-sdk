from typing import Literal

ApiV1CvesUpdateCvssScoreErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_CVES_UPDATE_CVSS_SCORE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesUpdateCvssScoreErrorComponentCode] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_cves_update_cvss_score_error_component_code(value: str) -> ApiV1CvesUpdateCvssScoreErrorComponentCode:
    if value in API_V1_CVES_UPDATE_CVSS_SCORE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_CVSS_SCORE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
