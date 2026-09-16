from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_downtimes_create_annotations_error_component import (
        ApiV1DowntimesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_downtimes_create_counts_towards_sla_error_component import (
        ApiV1DowntimesCreateCountsTowardsSlaErrorComponent,
    )
    from ..models.api_v1_downtimes_create_display_name_error_component import (
        ApiV1DowntimesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_downtimes_create_excluded_reason_error_component import (
        ApiV1DowntimesCreateExcludedReasonErrorComponent,
    )
    from ..models.api_v1_downtimes_create_is_active_error_component import ApiV1DowntimesCreateIsActiveErrorComponent
    from ..models.api_v1_downtimes_create_kind_error_component import ApiV1DowntimesCreateKindErrorComponent
    from ..models.api_v1_downtimes_create_labels_error_component import ApiV1DowntimesCreateLabelsErrorComponent
    from ..models.api_v1_downtimes_create_name_error_component import ApiV1DowntimesCreateNameErrorComponent
    from ..models.api_v1_downtimes_create_non_field_errors_error_component import (
        ApiV1DowntimesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_downtimes_create_post_mortem_content_error_component import (
        ApiV1DowntimesCreatePostMortemContentErrorComponent,
    )
    from ..models.api_v1_downtimes_create_post_mortem_note_id_error_component import (
        ApiV1DowntimesCreatePostMortemNoteIdErrorComponent,
    )
    from ..models.api_v1_downtimes_create_severity_error_component import ApiV1DowntimesCreateSeverityErrorComponent
    from ..models.api_v1_downtimes_create_tolerations_error_component import (
        ApiV1DowntimesCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DowntimesCreateValidationError")


@_attrs_define
class ApiV1DowntimesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DowntimesCreateAnnotationsErrorComponent | ApiV1DowntimesCreateCountsTowardsSlaErrorComponent
            | ApiV1DowntimesCreateDisplayNameErrorComponent | ApiV1DowntimesCreateExcludedReasonErrorComponent |
            ApiV1DowntimesCreateIsActiveErrorComponent | ApiV1DowntimesCreateKindErrorComponent |
            ApiV1DowntimesCreateLabelsErrorComponent | ApiV1DowntimesCreateNameErrorComponent |
            ApiV1DowntimesCreateNonFieldErrorsErrorComponent | ApiV1DowntimesCreatePostMortemContentErrorComponent |
            ApiV1DowntimesCreatePostMortemNoteIdErrorComponent | ApiV1DowntimesCreateSeverityErrorComponent |
            ApiV1DowntimesCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DowntimesCreateAnnotationsErrorComponent
        | ApiV1DowntimesCreateCountsTowardsSlaErrorComponent
        | ApiV1DowntimesCreateDisplayNameErrorComponent
        | ApiV1DowntimesCreateExcludedReasonErrorComponent
        | ApiV1DowntimesCreateIsActiveErrorComponent
        | ApiV1DowntimesCreateKindErrorComponent
        | ApiV1DowntimesCreateLabelsErrorComponent
        | ApiV1DowntimesCreateNameErrorComponent
        | ApiV1DowntimesCreateNonFieldErrorsErrorComponent
        | ApiV1DowntimesCreatePostMortemContentErrorComponent
        | ApiV1DowntimesCreatePostMortemNoteIdErrorComponent
        | ApiV1DowntimesCreateSeverityErrorComponent
        | ApiV1DowntimesCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_downtimes_create_annotations_error_component import (
            ApiV1DowntimesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_counts_towards_sla_error_component import (
            ApiV1DowntimesCreateCountsTowardsSlaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_display_name_error_component import (
            ApiV1DowntimesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_excluded_reason_error_component import (
            ApiV1DowntimesCreateExcludedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_is_active_error_component import (
            ApiV1DowntimesCreateIsActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_kind_error_component import (
            ApiV1DowntimesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_labels_error_component import (
            ApiV1DowntimesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_name_error_component import (
            ApiV1DowntimesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_non_field_errors_error_component import (
            ApiV1DowntimesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_post_mortem_content_error_component import (
            ApiV1DowntimesCreatePostMortemContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_severity_error_component import (
            ApiV1DowntimesCreateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_tolerations_error_component import (
            ApiV1DowntimesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DowntimesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreateIsActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreateCountsTowardsSlaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreateExcludedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesCreatePostMortemContentErrorComponent):
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
        from ..models.api_v1_downtimes_create_annotations_error_component import (
            ApiV1DowntimesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_counts_towards_sla_error_component import (
            ApiV1DowntimesCreateCountsTowardsSlaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_display_name_error_component import (
            ApiV1DowntimesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_excluded_reason_error_component import (
            ApiV1DowntimesCreateExcludedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_is_active_error_component import (
            ApiV1DowntimesCreateIsActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_kind_error_component import (
            ApiV1DowntimesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_labels_error_component import (
            ApiV1DowntimesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_name_error_component import (
            ApiV1DowntimesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_non_field_errors_error_component import (
            ApiV1DowntimesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_post_mortem_content_error_component import (
            ApiV1DowntimesCreatePostMortemContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_post_mortem_note_id_error_component import (
            ApiV1DowntimesCreatePostMortemNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_severity_error_component import (
            ApiV1DowntimesCreateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_create_tolerations_error_component import (
            ApiV1DowntimesCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DowntimesCreateAnnotationsErrorComponent
                | ApiV1DowntimesCreateCountsTowardsSlaErrorComponent
                | ApiV1DowntimesCreateDisplayNameErrorComponent
                | ApiV1DowntimesCreateExcludedReasonErrorComponent
                | ApiV1DowntimesCreateIsActiveErrorComponent
                | ApiV1DowntimesCreateKindErrorComponent
                | ApiV1DowntimesCreateLabelsErrorComponent
                | ApiV1DowntimesCreateNameErrorComponent
                | ApiV1DowntimesCreateNonFieldErrorsErrorComponent
                | ApiV1DowntimesCreatePostMortemContentErrorComponent
                | ApiV1DowntimesCreatePostMortemNoteIdErrorComponent
                | ApiV1DowntimesCreateSeverityErrorComponent
                | ApiV1DowntimesCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_0 = (
                        ApiV1DowntimesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_1 = (
                        ApiV1DowntimesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_2 = (
                        ApiV1DowntimesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_3 = (
                        ApiV1DowntimesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_4 = (
                        ApiV1DowntimesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_5 = (
                        ApiV1DowntimesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_6 = (
                        ApiV1DowntimesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_7 = (
                        ApiV1DowntimesCreateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_8 = (
                        ApiV1DowntimesCreateIsActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_9 = (
                        ApiV1DowntimesCreateCountsTowardsSlaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_10 = (
                        ApiV1DowntimesCreateExcludedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_create_error_type_11 = (
                        ApiV1DowntimesCreatePostMortemContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_downtimes_create_error_type_12 = (
                    ApiV1DowntimesCreatePostMortemNoteIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_downtimes_create_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_downtimes_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_downtimes_create_validation_error.additional_properties = d
        return api_v1_downtimes_create_validation_error

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
