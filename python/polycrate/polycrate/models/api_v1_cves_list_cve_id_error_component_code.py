from typing import Literal

ApiV1CvesListCveIdErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_CVES_LIST_CVE_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesListCveIdErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_cves_list_cve_id_error_component_code(value: str) -> ApiV1CvesListCveIdErrorComponentCode:
    if value in API_V1_CVES_LIST_CVE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_CVE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
