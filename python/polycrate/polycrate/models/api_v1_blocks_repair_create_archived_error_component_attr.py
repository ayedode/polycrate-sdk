from typing import Literal

ApiV1BlocksRepairCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BLOCKS_REPAIR_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_blocks_repair_create_archived_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateArchivedErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
