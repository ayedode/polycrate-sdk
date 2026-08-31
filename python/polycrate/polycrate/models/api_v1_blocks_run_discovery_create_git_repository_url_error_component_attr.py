from typing import Literal

ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponentAttr = Literal["git_repository_url"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponentAttr
] = {
    "git_repository_url",
}


def check_api_v1_blocks_run_discovery_create_git_repository_url_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateGitRepositoryUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_GIT_REPOSITORY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
