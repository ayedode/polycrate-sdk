from typing import Literal

ApiV1CvesUpdateCvssScoreErrorComponentAttr = Literal["cvss_score"]

API_V1_CVES_UPDATE_CVSS_SCORE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateCvssScoreErrorComponentAttr] = {
    "cvss_score",
}


def check_api_v1_cves_update_cvss_score_error_component_attr(value: str) -> ApiV1CvesUpdateCvssScoreErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_CVSS_SCORE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_CVSS_SCORE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
