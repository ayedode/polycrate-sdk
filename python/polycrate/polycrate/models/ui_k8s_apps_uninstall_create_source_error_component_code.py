from typing import Literal

UiK8SAppsUninstallCreateSourceErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

UI_K8S_APPS_UNINSTALL_CREATE_SOURCE_ERROR_COMPONENT_CODE_VALUES: set[
    UiK8SAppsUninstallCreateSourceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_ui_k8s_apps_uninstall_create_source_error_component_code(
    value: str,
) -> UiK8SAppsUninstallCreateSourceErrorComponentCode:
    if value in UI_K8S_APPS_UNINSTALL_CREATE_SOURCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UI_K8S_APPS_UNINSTALL_CREATE_SOURCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
