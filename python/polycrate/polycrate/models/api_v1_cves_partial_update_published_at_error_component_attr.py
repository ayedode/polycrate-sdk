from typing import Literal

ApiV1CvesPartialUpdatePublishedAtErrorComponentAttr = Literal["published_at"]

API_V1_CVES_PARTIAL_UPDATE_PUBLISHED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesPartialUpdatePublishedAtErrorComponentAttr
] = {
    "published_at",
}


def check_api_v1_cves_partial_update_published_at_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdatePublishedAtErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_PUBLISHED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_PUBLISHED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
