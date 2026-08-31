from typing import Literal

ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponentAttr = Literal["git_repository_url"]

API_V1_BLOCKS_DISCOVER_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponentAttr
] = {
    "git_repository_url",
}


def check_api_v1_blocks_discover_create_git_repository_url_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateGitRepositoryUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
