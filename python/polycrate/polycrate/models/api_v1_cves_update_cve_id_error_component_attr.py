from typing import Literal

ApiV1CvesUpdateCveIdErrorComponentAttr = Literal["cve_id"]

API_V1_CVES_UPDATE_CVE_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateCveIdErrorComponentAttr] = {
    "cve_id",
}


def check_api_v1_cves_update_cve_id_error_component_attr(value: str) -> ApiV1CvesUpdateCveIdErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_CVE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_CVE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
