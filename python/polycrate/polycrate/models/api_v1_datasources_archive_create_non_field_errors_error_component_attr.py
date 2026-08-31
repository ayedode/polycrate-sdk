from typing import Literal

ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_DATASOURCES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_datasources_archive_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1DatasourcesArchiveCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_DATASOURCES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_ARCHIVE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
