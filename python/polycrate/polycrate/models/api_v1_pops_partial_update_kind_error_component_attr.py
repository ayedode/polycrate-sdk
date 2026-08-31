from typing import Literal

ApiV1PopsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_POPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsPartialUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_pops_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
