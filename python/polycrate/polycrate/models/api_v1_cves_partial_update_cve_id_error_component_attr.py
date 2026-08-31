from typing import Literal

ApiV1CvesPartialUpdateCveIdErrorComponentAttr = Literal["cve_id"]

API_V1_CVES_PARTIAL_UPDATE_CVE_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesPartialUpdateCveIdErrorComponentAttr] = {
    "cve_id",
}


def check_api_v1_cves_partial_update_cve_id_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdateCveIdErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_CVE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_CVE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
