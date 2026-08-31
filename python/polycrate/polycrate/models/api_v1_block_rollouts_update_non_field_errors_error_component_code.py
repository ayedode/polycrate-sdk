from typing import Literal

ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCK_ROLLOUTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_block_rollouts_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
