from typing import Literal

ApiV1BlocksDiscoverCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_BLOCKS_DISCOVER_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_blocks_discover_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateSlaTargetErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
