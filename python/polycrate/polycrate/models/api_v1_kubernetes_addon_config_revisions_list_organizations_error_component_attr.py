from typing import Literal

ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_kubernetes_addon_config_revisions_list_organizations_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonConfigRevisionsListOrganizationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDON_CONFIG_REVISIONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
