from typing import Literal

ApiV1KubernetesAddonsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_KUBERNETES_ADDONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_kubernetes_addons_list_organizations_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsListOrganizationsErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
