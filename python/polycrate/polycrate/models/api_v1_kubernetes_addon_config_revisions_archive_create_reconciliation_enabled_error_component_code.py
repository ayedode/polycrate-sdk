from typing import Literal

ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_addon_config_revisions_archive_create_reconciliation_enabled_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsArchiveCreateReconciliationEnabledErrorComponentCode:
    if (
        value
        in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_ARCHIVE_CREATE_RECONCILIATION_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
