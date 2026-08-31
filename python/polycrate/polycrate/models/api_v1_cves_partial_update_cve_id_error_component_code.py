from typing import Literal

ApiV1CvesPartialUpdateCveIdErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
]

API_V1_CVES_PARTIAL_UPDATE_CVE_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesPartialUpdateCveIdErrorComponentCode] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
    "unique",
}


def check_api_v1_cves_partial_update_cve_id_error_component_code(
    value: str,
) -> ApiV1CvesPartialUpdateCveIdErrorComponentCode:
    if value in API_V1_CVES_PARTIAL_UPDATE_CVE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_CVE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
