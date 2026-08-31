from typing import Literal

ApiV1BlocksRepairCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_REPAIR_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRepairCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_repair_create_archived_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateArchivedErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
