from typing import Literal

ApiV1BlockRolloutsCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUTS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollouts_create_tolerations_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateTolerationsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
