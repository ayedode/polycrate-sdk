from typing import Literal

ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponentAttr = Literal["git_repository_url"]

API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponentAttr
] = {
    "git_repository_url",
}


def check_api_v1_catalogue_apps_archive_create_git_repository_url_error_component_attr(
    value: str,
) -> ApiV1CatalogueAppsArchiveCreateGitRepositoryUrlErrorComponentAttr:
    if value in API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CATALOGUE_APPS_ARCHIVE_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
