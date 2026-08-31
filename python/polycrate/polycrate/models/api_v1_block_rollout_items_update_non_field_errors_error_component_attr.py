from typing import Literal

ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_block_rollout_items_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
