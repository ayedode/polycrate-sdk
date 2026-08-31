from typing import Literal

ApiV1BlocksRepairCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_REPAIR_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksRepairCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_blocks_repair_create_labels_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateLabelsErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
