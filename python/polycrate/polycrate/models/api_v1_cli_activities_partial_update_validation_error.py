from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_cli_activities_partial_update_duration_seconds_error_component import (
        ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponent,
    )
    from ..models.api_v1_cli_activities_partial_update_exit_code_error_component import (
        ApiV1CliActivitiesPartialUpdateExitCodeErrorComponent,
    )
    from ..models.api_v1_cli_activities_partial_update_finished_at_error_component import (
        ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponent,
    )
    from ..models.api_v1_cli_activities_partial_update_non_field_errors_error_component import (
        ApiV1CliActivitiesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_cli_activities_partial_update_status_error_component import (
        ApiV1CliActivitiesPartialUpdateStatusErrorComponent,
    )


T = TypeVar("T", bound="ApiV1CliActivitiesPartialUpdateValidationError")


@_attrs_define
class ApiV1CliActivitiesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponent |
            ApiV1CliActivitiesPartialUpdateExitCodeErrorComponent | ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponent
            | ApiV1CliActivitiesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1CliActivitiesPartialUpdateStatusErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponent
        | ApiV1CliActivitiesPartialUpdateExitCodeErrorComponent
        | ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponent
        | ApiV1CliActivitiesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1CliActivitiesPartialUpdateStatusErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_cli_activities_partial_update_duration_seconds_error_component import (
            ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cli_activities_partial_update_exit_code_error_component import (
            ApiV1CliActivitiesPartialUpdateExitCodeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cli_activities_partial_update_finished_at_error_component import (
            ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cli_activities_partial_update_non_field_errors_error_component import (
            ApiV1CliActivitiesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1CliActivitiesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CliActivitiesPartialUpdateExitCodeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_cli_activities_partial_update_duration_seconds_error_component import (
            ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cli_activities_partial_update_exit_code_error_component import (
            ApiV1CliActivitiesPartialUpdateExitCodeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cli_activities_partial_update_finished_at_error_component import (
            ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cli_activities_partial_update_non_field_errors_error_component import (
            ApiV1CliActivitiesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_cli_activities_partial_update_status_error_component import (
            ApiV1CliActivitiesPartialUpdateStatusErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponent
                | ApiV1CliActivitiesPartialUpdateExitCodeErrorComponent
                | ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponent
                | ApiV1CliActivitiesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1CliActivitiesPartialUpdateStatusErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cli_activities_partial_update_error_type_0 = (
                        ApiV1CliActivitiesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cli_activities_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cli_activities_partial_update_error_type_1 = (
                        ApiV1CliActivitiesPartialUpdateExitCodeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cli_activities_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cli_activities_partial_update_error_type_2 = (
                        ApiV1CliActivitiesPartialUpdateFinishedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cli_activities_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_cli_activities_partial_update_error_type_3 = (
                        ApiV1CliActivitiesPartialUpdateDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_cli_activities_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_cli_activities_partial_update_error_type_4 = (
                    ApiV1CliActivitiesPartialUpdateStatusErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_cli_activities_partial_update_error_type_4

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_cli_activities_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_cli_activities_partial_update_validation_error.additional_properties = d
        return api_v1_cli_activities_partial_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
