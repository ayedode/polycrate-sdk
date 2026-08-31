from typing import Literal

ApiV1BlocksPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCKS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_blocks_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
