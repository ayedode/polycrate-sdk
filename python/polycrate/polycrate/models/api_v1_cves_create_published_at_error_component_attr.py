from typing import Literal

ApiV1CvesCreatePublishedAtErrorComponentAttr = Literal["published_at"]

API_V1_CVES_CREATE_PUBLISHED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreatePublishedAtErrorComponentAttr] = {
    "published_at",
}


def check_api_v1_cves_create_published_at_error_component_attr(
    value: str,
) -> ApiV1CvesCreatePublishedAtErrorComponentAttr:
    if value in API_V1_CVES_CREATE_PUBLISHED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_PUBLISHED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
