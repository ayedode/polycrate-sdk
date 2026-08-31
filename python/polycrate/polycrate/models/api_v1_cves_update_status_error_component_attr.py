from typing import Literal

ApiV1CvesUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_CVES_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_cves_update_status_error_component_attr(value: str) -> ApiV1CvesUpdateStatusErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
