from typing import Literal

ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_secretmanager_managers_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
