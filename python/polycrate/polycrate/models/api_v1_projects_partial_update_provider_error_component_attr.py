from typing import Literal

ApiV1ProjectsPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_PROJECTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProjectsPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_projects_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1ProjectsPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_PROJECTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
