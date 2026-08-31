from typing import Literal

ApiV1CvesCreateCveIdErrorComponentAttr = Literal["cve_id"]

API_V1_CVES_CREATE_CVE_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateCveIdErrorComponentAttr] = {
    "cve_id",
}


def check_api_v1_cves_create_cve_id_error_component_attr(value: str) -> ApiV1CvesCreateCveIdErrorComponentAttr:
    if value in API_V1_CVES_CREATE_CVE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_CVE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
