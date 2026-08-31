from typing import Literal

ApiV1BlocksUpdateAutoRolloutErrorComponentAttr = Literal["auto_rollout"]

API_V1_BLOCKS_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateAutoRolloutErrorComponentAttr] = {
    "auto_rollout",
}


def check_api_v1_blocks_update_auto_rollout_error_component_attr(
    value: str,
) -> ApiV1BlocksUpdateAutoRolloutErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
