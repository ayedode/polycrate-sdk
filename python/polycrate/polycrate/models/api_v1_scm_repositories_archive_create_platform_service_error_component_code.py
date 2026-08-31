from typing import Literal

ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_scm_repositories_archive_create_platform_service_error_component_code(
    value: str,
) -> ApiV1ScmRepositoriesArchiveCreatePlatformServiceErrorComponentCode:
    if value in API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
