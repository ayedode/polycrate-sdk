from typing import Literal

ApiV1DowntimesCreatePostMortemContentErrorComponentAttr = Literal["post_mortem_content"]

API_V1_DOWNTIMES_CREATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesCreatePostMortemContentErrorComponentAttr
] = {
    "post_mortem_content",
}


def check_api_v1_downtimes_create_post_mortem_content_error_component_attr(
    value: str,
) -> ApiV1DowntimesCreatePostMortemContentErrorComponentAttr:
    if value in API_V1_DOWNTIMES_CREATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
