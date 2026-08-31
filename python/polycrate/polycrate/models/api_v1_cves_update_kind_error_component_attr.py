from typing import Literal

ApiV1CvesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_CVES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_cves_update_kind_error_component_attr(value: str) -> ApiV1CvesUpdateKindErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
