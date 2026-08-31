from typing import Literal

ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_ORGANIZATIONS_RECONCILE_CREATE_LOOPBACK_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_organizations_reconcile_create_loopback_project_id_error_component_code(
    value: str,
) -> ApiV1OrganizationsReconcileCreateLoopbackProjectIdErrorComponentCode:
    if value in API_V1_ORGANIZATIONS_RECONCILE_CREATE_LOOPBACK_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_RECONCILE_CREATE_LOOPBACK_PROJECT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
