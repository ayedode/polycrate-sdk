from typing import Literal

ApiV1PopsUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_POPS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_pops_update_kind_error_component_attr(value: str) -> ApiV1PopsUpdateKindErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
