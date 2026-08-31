from typing import Literal

ApiV1BlocksCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_blocks_create_labels_error_component_code(value: str) -> ApiV1BlocksCreateLabelsErrorComponentCode:
    if value in API_V1_BLOCKS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
