from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_downtimes_update_annotations_error_component import (
        ApiV1DowntimesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_downtimes_update_counts_towards_sla_error_component import (
        ApiV1DowntimesUpdateCountsTowardsSlaErrorComponent,
    )
    from ..models.api_v1_downtimes_update_display_name_error_component import (
        ApiV1DowntimesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_downtimes_update_excluded_reason_error_component import (
        ApiV1DowntimesUpdateExcludedReasonErrorComponent,
    )
    from ..models.api_v1_downtimes_update_is_active_error_component import ApiV1DowntimesUpdateIsActiveErrorComponent
    from ..models.api_v1_downtimes_update_kind_error_component import ApiV1DowntimesUpdateKindErrorComponent
    from ..models.api_v1_downtimes_update_labels_error_component import ApiV1DowntimesUpdateLabelsErrorComponent
    from ..models.api_v1_downtimes_update_name_error_component import ApiV1DowntimesUpdateNameErrorComponent
    from ..models.api_v1_downtimes_update_non_field_errors_error_component import (
        ApiV1DowntimesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_downtimes_update_post_mortem_content_error_component import (
        ApiV1DowntimesUpdatePostMortemContentErrorComponent,
    )
    from ..models.api_v1_downtimes_update_post_mortem_note_id_error_component import (
        ApiV1DowntimesUpdatePostMortemNoteIdErrorComponent,
    )
    from ..models.api_v1_downtimes_update_severity_error_component import ApiV1DowntimesUpdateSeverityErrorComponent
    from ..models.api_v1_downtimes_update_tolerations_error_component import (
        ApiV1DowntimesUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DowntimesUpdateValidationError")


@_attrs_define
class ApiV1DowntimesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DowntimesUpdateAnnotationsErrorComponent | ApiV1DowntimesUpdateCountsTowardsSlaErrorComponent
            | ApiV1DowntimesUpdateDisplayNameErrorComponent | ApiV1DowntimesUpdateExcludedReasonErrorComponent |
            ApiV1DowntimesUpdateIsActiveErrorComponent | ApiV1DowntimesUpdateKindErrorComponent |
            ApiV1DowntimesUpdateLabelsErrorComponent | ApiV1DowntimesUpdateNameErrorComponent |
            ApiV1DowntimesUpdateNonFieldErrorsErrorComponent | ApiV1DowntimesUpdatePostMortemContentErrorComponent |
            ApiV1DowntimesUpdatePostMortemNoteIdErrorComponent | ApiV1DowntimesUpdateSeverityErrorComponent |
            ApiV1DowntimesUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DowntimesUpdateAnnotationsErrorComponent
        | ApiV1DowntimesUpdateCountsTowardsSlaErrorComponent
        | ApiV1DowntimesUpdateDisplayNameErrorComponent
        | ApiV1DowntimesUpdateExcludedReasonErrorComponent
        | ApiV1DowntimesUpdateIsActiveErrorComponent
        | ApiV1DowntimesUpdateKindErrorComponent
        | ApiV1DowntimesUpdateLabelsErrorComponent
        | ApiV1DowntimesUpdateNameErrorComponent
        | ApiV1DowntimesUpdateNonFieldErrorsErrorComponent
        | ApiV1DowntimesUpdatePostMortemContentErrorComponent
        | ApiV1DowntimesUpdatePostMortemNoteIdErrorComponent
        | ApiV1DowntimesUpdateSeverityErrorComponent
        | ApiV1DowntimesUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_downtimes_update_annotations_error_component import (
            ApiV1DowntimesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_counts_towards_sla_error_component import (
            ApiV1DowntimesUpdateCountsTowardsSlaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_display_name_error_component import (
            ApiV1DowntimesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_excluded_reason_error_component import (
            ApiV1DowntimesUpdateExcludedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_is_active_error_component import (
            ApiV1DowntimesUpdateIsActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_kind_error_component import (
            ApiV1DowntimesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_labels_error_component import (
            ApiV1DowntimesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_name_error_component import (
            ApiV1DowntimesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_non_field_errors_error_component import (
            ApiV1DowntimesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_post_mortem_content_error_component import (
            ApiV1DowntimesUpdatePostMortemContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_severity_error_component import (
            ApiV1DowntimesUpdateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_tolerations_error_component import (
            ApiV1DowntimesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DowntimesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdateIsActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdateCountsTowardsSlaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdateExcludedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesUpdatePostMortemContentErrorComponent):
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
        from ..models.api_v1_downtimes_update_annotations_error_component import (
            ApiV1DowntimesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_counts_towards_sla_error_component import (
            ApiV1DowntimesUpdateCountsTowardsSlaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_display_name_error_component import (
            ApiV1DowntimesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_excluded_reason_error_component import (
            ApiV1DowntimesUpdateExcludedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_is_active_error_component import (
            ApiV1DowntimesUpdateIsActiveErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_kind_error_component import (
            ApiV1DowntimesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_labels_error_component import (
            ApiV1DowntimesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_name_error_component import (
            ApiV1DowntimesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_non_field_errors_error_component import (
            ApiV1DowntimesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_post_mortem_content_error_component import (
            ApiV1DowntimesUpdatePostMortemContentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_post_mortem_note_id_error_component import (
            ApiV1DowntimesUpdatePostMortemNoteIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_severity_error_component import (
            ApiV1DowntimesUpdateSeverityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_downtimes_update_tolerations_error_component import (
            ApiV1DowntimesUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DowntimesUpdateAnnotationsErrorComponent
                | ApiV1DowntimesUpdateCountsTowardsSlaErrorComponent
                | ApiV1DowntimesUpdateDisplayNameErrorComponent
                | ApiV1DowntimesUpdateExcludedReasonErrorComponent
                | ApiV1DowntimesUpdateIsActiveErrorComponent
                | ApiV1DowntimesUpdateKindErrorComponent
                | ApiV1DowntimesUpdateLabelsErrorComponent
                | ApiV1DowntimesUpdateNameErrorComponent
                | ApiV1DowntimesUpdateNonFieldErrorsErrorComponent
                | ApiV1DowntimesUpdatePostMortemContentErrorComponent
                | ApiV1DowntimesUpdatePostMortemNoteIdErrorComponent
                | ApiV1DowntimesUpdateSeverityErrorComponent
                | ApiV1DowntimesUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_0 = (
                        ApiV1DowntimesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_1 = (
                        ApiV1DowntimesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_2 = (
                        ApiV1DowntimesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_3 = (
                        ApiV1DowntimesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_4 = (
                        ApiV1DowntimesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_5 = (
                        ApiV1DowntimesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_6 = (
                        ApiV1DowntimesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_7 = (
                        ApiV1DowntimesUpdateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_8 = (
                        ApiV1DowntimesUpdateIsActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_9 = (
                        ApiV1DowntimesUpdateCountsTowardsSlaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_10 = (
                        ApiV1DowntimesUpdateExcludedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_update_error_type_11 = (
                        ApiV1DowntimesUpdatePostMortemContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_downtimes_update_error_type_12 = (
                    ApiV1DowntimesUpdatePostMortemNoteIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_downtimes_update_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_downtimes_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_downtimes_update_validation_error.additional_properties = d
        return api_v1_downtimes_update_validation_error

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
