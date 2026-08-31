from typing import Literal

ApiV1BlocksPartialUpdateLatestStableErrorComponentAttr = Literal["latest_stable"]

API_V1_BLOCKS_PARTIAL_UPDATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateLatestStableErrorComponentAttr
] = {
    "latest_stable",
}


def check_api_v1_blocks_partial_update_latest_stable_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateLatestStableErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
