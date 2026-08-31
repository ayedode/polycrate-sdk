from typing import Literal

ApiV1CvesPartialUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_CVES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesPartialUpdateStatusErrorComponentAttr] = {
    "status",
}


def check_api_v1_cves_partial_update_status_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdateStatusErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
