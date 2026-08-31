from typing import Literal

UiK8SAppsUninstallCreateDescriptionErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

UI_K8S_APPS_UNINSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateDescriptionErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_ui_k8s_apps_uninstall_create_description_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateDescriptionErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
