from typing import Literal

ApiV1BlocksCreateIsBehindStableErrorComponentAttr = Literal["is_behind_stable"]

API_V1_BLOCKS_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCreateIsBehindStableErrorComponentAttr
] = {
    "is_behind_stable",
}


def check_api_v1_blocks_create_is_behind_stable_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateIsBehindStableErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_IS_BEHIND_STABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
