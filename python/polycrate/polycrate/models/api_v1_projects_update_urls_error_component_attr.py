from typing import Literal

ApiV1ProjectsUpdateUrlsErrorComponentAttr = Literal["urls"]

API_V1_PROJECTS_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsUpdateUrlsErrorComponentAttr] = {
    "urls",
}


def check_api_v1_projects_update_urls_error_component_attr(value: str) -> ApiV1ProjectsUpdateUrlsErrorComponentAttr:
    if value in API_V1_PROJECTS_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_UPDATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
