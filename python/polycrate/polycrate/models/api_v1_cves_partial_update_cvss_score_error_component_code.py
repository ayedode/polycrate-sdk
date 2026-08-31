from typing import Literal

ApiV1CvesPartialUpdateCvssScoreErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_CVES_PARTIAL_UPDATE_CVSS_SCORE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CvesPartialUpdateCvssScoreErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_cves_partial_update_cvss_score_error_component_code(
    value: str,
) -> ApiV1CvesPartialUpdateCvssScoreErrorComponentCode:
    if value in API_V1_CVES_PARTIAL_UPDATE_CVSS_SCORE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_CVSS_SCORE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
