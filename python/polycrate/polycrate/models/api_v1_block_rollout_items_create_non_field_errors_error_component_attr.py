from typing import Literal

ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_block_rollout_items_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_ITEMS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
