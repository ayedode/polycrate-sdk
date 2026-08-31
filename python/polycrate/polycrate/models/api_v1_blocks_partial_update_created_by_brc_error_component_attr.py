from typing import Literal

ApiV1BlocksPartialUpdateCreatedByBrcErrorComponentAttr = Literal["created_by_brc"]

API_V1_BLOCKS_PARTIAL_UPDATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateCreatedByBrcErrorComponentAttr
] = {
    "created_by_brc",
}


def check_api_v1_blocks_partial_update_created_by_brc_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateCreatedByBrcErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
