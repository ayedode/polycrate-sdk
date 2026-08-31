from typing import Literal

ApiV1ProjectsCreateUrlsErrorComponentAttr = Literal["urls"]

API_V1_PROJECTS_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsCreateUrlsErrorComponentAttr] = {
    "urls",
}


def check_api_v1_projects_create_urls_error_component_attr(value: str) -> ApiV1ProjectsCreateUrlsErrorComponentAttr:
    if value in API_V1_PROJECTS_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_URLS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
