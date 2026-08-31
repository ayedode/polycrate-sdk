from typing import Literal

ApiV1BlocksUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCKS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_blocks_update_kind_error_component_attr(value: str) -> ApiV1BlocksUpdateKindErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
