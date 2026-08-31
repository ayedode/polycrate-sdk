from typing import Literal

ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_DATASOURCES_INGEST_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_datasources_ingest_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1DatasourcesIngestCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_DATASOURCES_INGEST_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_INGEST_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
