from typing import Literal

ApiV1ScmRepositoriesCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_SCM_REPOSITORIES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ScmRepositoriesCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_scm_repositories_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1ScmRepositoriesCreateSlaTargetErrorComponentAttr:
    if value in API_V1_SCM_REPOSITORIES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SCM_REPOSITORIES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
