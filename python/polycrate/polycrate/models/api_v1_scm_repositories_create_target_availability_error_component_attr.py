from typing import Literal

ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_SCM_REPOSITORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_scm_repositories_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
