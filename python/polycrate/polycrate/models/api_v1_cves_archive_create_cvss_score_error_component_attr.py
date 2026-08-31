from typing import Literal

ApiV1CvesArchiveCreateCvssScoreErrorComponentAttr = Literal["cvss_score"]

API_V1_CVES_ARCHIVE_CREATE_CVSS_SCORE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesArchiveCreateCvssScoreErrorComponentAttr
] = {
    "cvss_score",
}


def check_api_v1_cves_archive_create_cvss_score_error_component_attr(
    value: str,
) -> ApiV1CvesArchiveCreateCvssScoreErrorComponentAttr:
    if value in API_V1_CVES_ARCHIVE_CREATE_CVSS_SCORE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_CVSS_SCORE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
