from typing import Literal

ApiV1BlocksPartialUpdateAutoRolloutErrorComponentAttr = Literal["auto_rollout"]

API_V1_BLOCKS_PARTIAL_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateAutoRolloutErrorComponentAttr
] = {
    "auto_rollout",
}


def check_api_v1_blocks_partial_update_auto_rollout_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateAutoRolloutErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
