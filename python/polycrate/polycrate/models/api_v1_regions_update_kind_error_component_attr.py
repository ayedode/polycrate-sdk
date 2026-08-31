from typing import Literal

ApiV1RegionsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_REGIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_regions_update_kind_error_component_attr(value: str) -> ApiV1RegionsUpdateKindErrorComponentAttr:
    if value in API_V1_REGIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
