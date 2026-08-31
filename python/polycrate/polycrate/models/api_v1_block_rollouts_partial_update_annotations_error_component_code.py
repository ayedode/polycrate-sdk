from typing import Literal

ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollouts_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
