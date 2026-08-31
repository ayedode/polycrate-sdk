from typing import Literal

ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponentAttr = Literal["git_repository_url"]

API_V1_BLOCKS_CHECK_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponentAttr
] = {
    "git_repository_url",
}


def check_api_v1_blocks_check_create_git_repository_url_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateGitRepositoryUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
