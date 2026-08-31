from typing import Literal

ApiV1BlockRolloutsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollouts_create_annotations_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateAnnotationsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
