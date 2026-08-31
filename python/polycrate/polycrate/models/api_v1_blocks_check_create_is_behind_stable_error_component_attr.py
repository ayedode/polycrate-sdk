from typing import Literal

ApiV1BlocksCheckCreateIsBehindStableErrorComponentAttr = Literal["is_behind_stable"]

API_V1_BLOCKS_CHECK_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateIsBehindStableErrorComponentAttr
] = {
    "is_behind_stable",
}


def check_api_v1_blocks_check_create_is_behind_stable_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateIsBehindStableErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
