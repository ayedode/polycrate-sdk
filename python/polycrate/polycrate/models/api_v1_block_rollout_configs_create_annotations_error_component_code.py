from typing import Literal

ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_block_rollout_configs_create_annotations_error_component_code(
    value: str,
) -> ApiV1BlockRolloutConfigsCreateAnnotationsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
