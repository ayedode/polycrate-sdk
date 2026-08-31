from typing import Literal

ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponentAttr = Literal["git_repository_url"]

API_V1_CATALOGUE_APPS_UPDATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponentAttr
] = {
    "git_repository_url",
}


def check_api_v1_catalogue_apps_update_git_repository_url_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsUpdateGitRepositoryUrlErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_UPDATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_UPDATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
