from typing import Literal

ApiV1BlocksCreateLatestStableErrorComponentAttr = Literal["latest_stable"]

API_V1_BLOCKS_CREATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateLatestStableErrorComponentAttr] = {
    "latest_stable",
}


def check_api_v1_blocks_create_latest_stable_error_component_attr(
    value: str,
) -> ApiV1BlocksCreateLatestStableErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
