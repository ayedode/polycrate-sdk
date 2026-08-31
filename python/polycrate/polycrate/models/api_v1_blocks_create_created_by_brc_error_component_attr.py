from typing import Literal

ApiV1BlocksCreateCreatedByBrcErrorComponentAttr = Literal["created_by_brc"]

API_V1_BLOCKS_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCreateCreatedByBrcErrorComponentAttr
] = {
    "created_by_brc",
}


def check_api_v1_blocks_create_created_by_brc_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateCreatedByBrcErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_CREATED_BY_BRC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
