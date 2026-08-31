from typing import Literal

ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_block_rollout_configs_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
