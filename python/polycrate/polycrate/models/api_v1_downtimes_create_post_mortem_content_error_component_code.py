from typing import Literal

ApiV1DowntimesCreatePostMortemContentErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_DOWNTIMES_CREATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DowntimesCreatePostMortemContentErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_downtimes_create_post_mortem_content_error_component_code(
    value: str,
) -> ApiV1DowntimesCreatePostMortemContentErrorComponentCode:
    if value in API_V1_DOWNTIMES_CREATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_CREATE_POST_MORTEM_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
