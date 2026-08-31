from typing import Literal

ApiV1ArtifactsUpdateWebsiteUrlErrorComponentAttr = Literal["website_url"]

API_V1_ARTIFACTS_UPDATE_WEBSITE_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateWebsiteUrlErrorComponentAttr
] = {
    "website_url",
}


def check_api_v1_artifacts_update_website_url_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateWebsiteUrlErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_WEBSITE_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_WEBSITE_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
