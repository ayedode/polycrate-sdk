from typing import Literal

ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponentAttr = Literal["policies_count"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_POLICIES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponentAttr
] = {
    "policies_count",
}


def check_api_v1_secretmanager_managers_update_policies_count_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdatePoliciesCountErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_POLICIES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_POLICIES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
