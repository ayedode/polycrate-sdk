from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_downtimes_archive_create_annotations_error_component import (
        ApiV1DowntimesArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_counts_towards_sla_error_component import (
        ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_display_name_error_component import (
        ApiV1DowntimesArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_excluded_reason_error_component import (
        ApiV1DowntimesArchiveCreateExcludedReasonErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_is_active_error_component import (
        ApiV1DowntimesArchiveCreateIsActiveErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_kind_error_component import (
        ApiV1DowntimesArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_labels_error_component import (
        ApiV1DowntimesArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_name_error_component import (
        ApiV1DowntimesArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_non_field_errors_error_component import (
        ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_post_mortem_content_error_component import (
        ApiV1DowntimesArchiveCreatePostMortemContentErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_post_mortem_note_id_error_component import (
        ApiV1DowntimesArchiveCreatePostMortemNoteIdErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_severity_error_component import (
        ApiV1DowntimesArchiveCreateSeverityErrorComponent,
    )
    from ..models.api_v1_downtimes_archive_create_tolerations_error_component import (
        ApiV1DowntimesArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DowntimesArchiveCreateValidationError")


@_attrs_define
class ApiV1DowntimesArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DowntimesArchiveCreateAnnotationsErrorComponent |
            ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponent | ApiV1DowntimesArchiveCreateDisplayNameErrorComponent
            | ApiV1DowntimesArchiveCreateExcludedReasonErrorComponent | ApiV1DowntimesArchiveCreateIsActiveErrorComponent |
            ApiV1DowntimesArchiveCreateKindErrorComponent | ApiV1DowntimesArchiveCreateLabelsErrorComponent |
            ApiV1DowntimesArchiveCreateNameErrorComponent | ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1DowntimesArchiveCreatePostMortemContentErrorComponent |
            ApiV1DowntimesArchiveCreatePostMortemNoteIdErrorComponent | ApiV1DowntimesArchiveCreateSeverityErrorComponent |
            ApiV1DowntimesArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DowntimesArchiveCreateAnnotationsErrorComponent
        | ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponent
        | ApiV1DowntimesArchiveCreateDisplayNameErrorComponent
        | ApiV1DowntimesArchiveCreateExcludedReasonErrorComponent
        | ApiV1DowntimesArchiveCreateIsActiveErrorComponent
        | ApiV1DowntimesArchiveCreateKindErrorComponent
        | ApiV1DowntimesArchiveCreateLabelsErrorComponent
        | ApiV1DowntimesArchiveCreateNameErrorComponent
        | ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1DowntimesArchiveCreatePostMortemContentErrorComponent
        | ApiV1DowntimesArchiveCreatePostMortemNoteIdErrorComponent
        | ApiV1DowntimesArchiveCreateSeverityErrorComponent
        | ApiV1DowntimesArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_downtimes_archive_create_annotations_error_component import (
            ApiV1DowntimesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_counts_towards_sla_error_component import (
            ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_display_name_error_component import (
            ApiV1DowntimesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_excluded_reason_error_component import (
            ApiV1DowntimesArchiveCreateExcludedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_is_active_error_component import (
            ApiV1DowntimesArchiveCreateIsActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_kind_error_component import (
            ApiV1DowntimesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_labels_error_component import (
            ApiV1DowntimesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_name_error_component import (
            ApiV1DowntimesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_non_field_errors_error_component import (
            ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_post_mortem_content_error_component import (
            ApiV1DowntimesArchiveCreatePostMortemContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_severity_error_component import (
            ApiV1DowntimesArchiveCreateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_tolerations_error_component import (
            ApiV1DowntimesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreateIsActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreateExcludedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesArchiveCreatePostMortemContentErrorComponent):
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
        from ..models.api_v1_downtimes_archive_create_annotations_error_component import (
            ApiV1DowntimesArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_counts_towards_sla_error_component import (
            ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_display_name_error_component import (
            ApiV1DowntimesArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_excluded_reason_error_component import (
            ApiV1DowntimesArchiveCreateExcludedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_is_active_error_component import (
            ApiV1DowntimesArchiveCreateIsActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_kind_error_component import (
            ApiV1DowntimesArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_labels_error_component import (
            ApiV1DowntimesArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_name_error_component import (
            ApiV1DowntimesArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_non_field_errors_error_component import (
            ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_post_mortem_content_error_component import (
            ApiV1DowntimesArchiveCreatePostMortemContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_post_mortem_note_id_error_component import (
            ApiV1DowntimesArchiveCreatePostMortemNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_severity_error_component import (
            ApiV1DowntimesArchiveCreateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_archive_create_tolerations_error_component import (
            ApiV1DowntimesArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DowntimesArchiveCreateAnnotationsErrorComponent
                | ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponent
                | ApiV1DowntimesArchiveCreateDisplayNameErrorComponent
                | ApiV1DowntimesArchiveCreateExcludedReasonErrorComponent
                | ApiV1DowntimesArchiveCreateIsActiveErrorComponent
                | ApiV1DowntimesArchiveCreateKindErrorComponent
                | ApiV1DowntimesArchiveCreateLabelsErrorComponent
                | ApiV1DowntimesArchiveCreateNameErrorComponent
                | ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1DowntimesArchiveCreatePostMortemContentErrorComponent
                | ApiV1DowntimesArchiveCreatePostMortemNoteIdErrorComponent
                | ApiV1DowntimesArchiveCreateSeverityErrorComponent
                | ApiV1DowntimesArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_0 = (
                        ApiV1DowntimesArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_1 = (
                        ApiV1DowntimesArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_2 = (
                        ApiV1DowntimesArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_3 = (
                        ApiV1DowntimesArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_4 = (
                        ApiV1DowntimesArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_5 = (
                        ApiV1DowntimesArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_6 = (
                        ApiV1DowntimesArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_7 = (
                        ApiV1DowntimesArchiveCreateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_8 = (
                        ApiV1DowntimesArchiveCreateIsActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_9 = (
                        ApiV1DowntimesArchiveCreateCountsTowardsSlaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_10 = (
                        ApiV1DowntimesArchiveCreateExcludedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_archive_create_error_type_11 = (
                        ApiV1DowntimesArchiveCreatePostMortemContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_downtimes_archive_create_error_type_12 = (
                    ApiV1DowntimesArchiveCreatePostMortemNoteIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_downtimes_archive_create_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_downtimes_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_downtimes_archive_create_validation_error.additional_properties = d
        return api_v1_downtimes_archive_create_validation_error

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
