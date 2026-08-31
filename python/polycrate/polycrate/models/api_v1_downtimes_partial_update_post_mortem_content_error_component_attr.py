from typing import Literal

ApiV1DowntimesPartialUpdatePostMortemContentErrorComponentAttr = Literal["post_mortem_content"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesPartialUpdatePostMortemContentErrorComponentAttr
] = {
    "post_mortem_content",
}


def check_api_v1_downtimes_partial_update_post_mortem_content_error_component_attr(
    value: str,
) -> ApiV1DowntimesPartialUpdatePostMortemContentErrorComponentAttr:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
