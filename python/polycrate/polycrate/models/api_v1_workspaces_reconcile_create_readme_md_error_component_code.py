from typing import Literal

ApiV1WorkspacesReconcileCreateReadmeMdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_WORKSPACES_RECONCILE_CREATE_README_MD_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReconcileCreateReadmeMdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_workspaces_reconcile_create_readme_md_error_component_code(
    value: str,
) -> ApiV1WorkspacesReconcileCreateReadmeMdErrorComponentCode:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_README_MD_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_README_MD_ERROR_COMPONENT_CODE_VALUES!r}"
    )
