from typing import Literal

ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponentAttr = Literal["policies_count"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_POLICIES_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponentAttr
] = {
    "policies_count",
}


def check_api_v1_secretmanager_managers_archive_create_policies_count_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreatePoliciesCountErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_POLICIES_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_POLICIES_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
