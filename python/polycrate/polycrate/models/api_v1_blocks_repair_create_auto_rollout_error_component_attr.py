from typing import Literal

ApiV1BlocksRepairCreateAutoRolloutErrorComponentAttr = Literal["auto_rollout"]

API_V1_BLOCKS_REPAIR_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateAutoRolloutErrorComponentAttr
] = {
    "auto_rollout",
}


def check_api_v1_blocks_repair_create_auto_rollout_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateAutoRolloutErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
