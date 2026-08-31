from typing import Literal

ApiV1BlocksRepairCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_REPAIR_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksRepairCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_repair_create_annotations_error_component_code(
    value: str,
) -> ApiV1BlocksRepairCreateAnnotationsErrorComponentCode:
    if value in API_V1_BLOCKS_REPAIR_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
