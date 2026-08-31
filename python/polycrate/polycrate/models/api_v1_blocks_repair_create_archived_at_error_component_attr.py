from typing import Literal

ApiV1BlocksRepairCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_BLOCKS_REPAIR_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_blocks_repair_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateArchivedAtErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
