from typing import Literal

ApiV1ProjectsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PROJECTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProjectsCreateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_projects_create_provider_error_component_attr(
    value: str,
) -> ApiV1ProjectsCreateProviderErrorComponentAttr:
    if value in API_V1_PROJECTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
