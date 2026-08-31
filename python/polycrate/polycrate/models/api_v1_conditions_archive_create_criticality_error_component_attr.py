from typing import Literal

ApiV1ConditionsArchiveCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CONDITIONS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsArchiveCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_conditions_archive_create_criticality_error_component_attr(
    value: str,
) -> ApiV1ConditionsArchiveCreateCriticalityErrorComponentAttr:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
