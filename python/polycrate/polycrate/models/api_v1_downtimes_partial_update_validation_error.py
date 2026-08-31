from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_downtimes_partial_update_annotations_error_component import (
        ApiV1DowntimesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_counts_towards_sla_error_component import (
        ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_display_name_error_component import (
        ApiV1DowntimesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_excluded_reason_error_component import (
        ApiV1DowntimesPartialUpdateExcludedReasonErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_is_active_error_component import (
        ApiV1DowntimesPartialUpdateIsActiveErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_kind_error_component import (
        ApiV1DowntimesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_labels_error_component import (
        ApiV1DowntimesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_name_error_component import (
        ApiV1DowntimesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_non_field_errors_error_component import (
        ApiV1DowntimesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_post_mortem_content_error_component import (
        ApiV1DowntimesPartialUpdatePostMortemContentErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_post_mortem_note_id_error_component import (
        ApiV1DowntimesPartialUpdatePostMortemNoteIdErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_severity_error_component import (
        ApiV1DowntimesPartialUpdateSeverityErrorComponent,
    )
    from ..models.api_v1_downtimes_partial_update_tolerations_error_component import (
        ApiV1DowntimesPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DowntimesPartialUpdateValidationError")


@_attrs_define
class ApiV1DowntimesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DowntimesPartialUpdateAnnotationsErrorComponent |
            ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponent | ApiV1DowntimesPartialUpdateDisplayNameErrorComponent
            | ApiV1DowntimesPartialUpdateExcludedReasonErrorComponent | ApiV1DowntimesPartialUpdateIsActiveErrorComponent |
            ApiV1DowntimesPartialUpdateKindErrorComponent | ApiV1DowntimesPartialUpdateLabelsErrorComponent |
            ApiV1DowntimesPartialUpdateNameErrorComponent | ApiV1DowntimesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1DowntimesPartialUpdatePostMortemContentErrorComponent |
            ApiV1DowntimesPartialUpdatePostMortemNoteIdErrorComponent | ApiV1DowntimesPartialUpdateSeverityErrorComponent |
            ApiV1DowntimesPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DowntimesPartialUpdateAnnotationsErrorComponent
        | ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponent
        | ApiV1DowntimesPartialUpdateDisplayNameErrorComponent
        | ApiV1DowntimesPartialUpdateExcludedReasonErrorComponent
        | ApiV1DowntimesPartialUpdateIsActiveErrorComponent
        | ApiV1DowntimesPartialUpdateKindErrorComponent
        | ApiV1DowntimesPartialUpdateLabelsErrorComponent
        | ApiV1DowntimesPartialUpdateNameErrorComponent
        | ApiV1DowntimesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1DowntimesPartialUpdatePostMortemContentErrorComponent
        | ApiV1DowntimesPartialUpdatePostMortemNoteIdErrorComponent
        | ApiV1DowntimesPartialUpdateSeverityErrorComponent
        | ApiV1DowntimesPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_downtimes_partial_update_annotations_error_component import (
            ApiV1DowntimesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_counts_towards_sla_error_component import (
            ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_display_name_error_component import (
            ApiV1DowntimesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_excluded_reason_error_component import (
            ApiV1DowntimesPartialUpdateExcludedReasonErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_is_active_error_component import (
            ApiV1DowntimesPartialUpdateIsActiveErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_kind_error_component import (
            ApiV1DowntimesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_labels_error_component import (
            ApiV1DowntimesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_name_error_component import (
            ApiV1DowntimesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_non_field_errors_error_component import (
            ApiV1DowntimesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_post_mortem_content_error_component import (
            ApiV1DowntimesPartialUpdatePostMortemContentErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_severity_error_component import (
            ApiV1DowntimesPartialUpdateSeverityErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_tolerations_error_component import (
            ApiV1DowntimesPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DowntimesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdateSeverityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdateIsActiveErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdateExcludedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DowntimesPartialUpdatePostMortemContentErrorComponent):
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
        from ..models.api_v1_downtimes_partial_update_annotations_error_component import (
            ApiV1DowntimesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_counts_towards_sla_error_component import (
            ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_display_name_error_component import (
            ApiV1DowntimesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_excluded_reason_error_component import (
            ApiV1DowntimesPartialUpdateExcludedReasonErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_is_active_error_component import (
            ApiV1DowntimesPartialUpdateIsActiveErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_kind_error_component import (
            ApiV1DowntimesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_labels_error_component import (
            ApiV1DowntimesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_name_error_component import (
            ApiV1DowntimesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_non_field_errors_error_component import (
            ApiV1DowntimesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_post_mortem_content_error_component import (
            ApiV1DowntimesPartialUpdatePostMortemContentErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_post_mortem_note_id_error_component import (
            ApiV1DowntimesPartialUpdatePostMortemNoteIdErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_severity_error_component import (
            ApiV1DowntimesPartialUpdateSeverityErrorComponent,
        )
        from ..models.api_v1_downtimes_partial_update_tolerations_error_component import (
            ApiV1DowntimesPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DowntimesPartialUpdateAnnotationsErrorComponent
                | ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponent
                | ApiV1DowntimesPartialUpdateDisplayNameErrorComponent
                | ApiV1DowntimesPartialUpdateExcludedReasonErrorComponent
                | ApiV1DowntimesPartialUpdateIsActiveErrorComponent
                | ApiV1DowntimesPartialUpdateKindErrorComponent
                | ApiV1DowntimesPartialUpdateLabelsErrorComponent
                | ApiV1DowntimesPartialUpdateNameErrorComponent
                | ApiV1DowntimesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1DowntimesPartialUpdatePostMortemContentErrorComponent
                | ApiV1DowntimesPartialUpdatePostMortemNoteIdErrorComponent
                | ApiV1DowntimesPartialUpdateSeverityErrorComponent
                | ApiV1DowntimesPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_0 = (
                        ApiV1DowntimesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_1 = (
                        ApiV1DowntimesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_2 = (
                        ApiV1DowntimesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_3 = (
                        ApiV1DowntimesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_4 = (
                        ApiV1DowntimesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_5 = (
                        ApiV1DowntimesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_6 = (
                        ApiV1DowntimesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_7 = (
                        ApiV1DowntimesPartialUpdateSeverityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_8 = (
                        ApiV1DowntimesPartialUpdateIsActiveErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_9 = (
                        ApiV1DowntimesPartialUpdateCountsTowardsSlaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_10 = (
                        ApiV1DowntimesPartialUpdateExcludedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_downtimes_partial_update_error_type_11 = (
                        ApiV1DowntimesPartialUpdatePostMortemContentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_downtimes_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_downtimes_partial_update_error_type_12 = (
                    ApiV1DowntimesPartialUpdatePostMortemNoteIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_downtimes_partial_update_error_type_12

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_downtimes_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_downtimes_partial_update_validation_error.additional_properties = d
        return api_v1_downtimes_partial_update_validation_error

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
