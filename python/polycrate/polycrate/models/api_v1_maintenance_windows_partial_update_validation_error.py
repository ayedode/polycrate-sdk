from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenance_windows_partial_update_annotations_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_archived_at_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_archived_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_archived_reason_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_criticality_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_debug_mode_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_description_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_display_name_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_is_system_default_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateIsSystemDefaultErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_kind_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_labels_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_lead_time_days_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_name_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_non_field_errors_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_note_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_notice_required_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_platform_service_error_component import (
        ApiV1MaintenanceWindowsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_provider_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_provider_id_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_provider_reference_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_reconciliation_enabled_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_sla_availability_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_sla_target_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_slo_availability_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_slo_target_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_target_availability_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_time_slots_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateTimeSlotsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_partial_update_tolerations_error_component import (
        ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenanceWindowsPartialUpdateValidationError")


@_attrs_define
class ApiV1MaintenanceWindowsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateArchivedAtErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateArchivedReasonErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateDebugModeErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateDescriptionErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateDisplayNameErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateIsSystemDefaultErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateKindErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateLabelsErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateNameErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdatePlatformServiceErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateProviderErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateProviderIdErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateProviderReferenceErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateSlaTargetErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateSloTargetErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateTimeSlotsErrorComponent |
            ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateArchivedAtErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateArchivedReasonErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateDebugModeErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateDescriptionErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateDisplayNameErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateIsSystemDefaultErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateKindErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateLabelsErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateNameErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdatePlatformServiceErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateProviderErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateProviderIdErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateProviderReferenceErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateSlaTargetErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateSloTargetErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateTimeSlotsErrorComponent
        | ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenance_windows_partial_update_annotations_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_archived_at_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_archived_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_archived_reason_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_criticality_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_debug_mode_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_description_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_display_name_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_is_system_default_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateIsSystemDefaultErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_kind_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_labels_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_lead_time_days_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_name_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_non_field_errors_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_note_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_notice_required_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_platform_service_error_component import (
            ApiV1MaintenanceWindowsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_provider_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_provider_id_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_provider_reference_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_reconciliation_enabled_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_sla_availability_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_sla_target_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_slo_availability_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_slo_target_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_target_availability_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_tolerations_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateIsSystemDefaultErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponent):
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
        from ..models.api_v1_maintenance_windows_partial_update_annotations_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_archived_at_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_archived_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_archived_reason_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_criticality_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_debug_mode_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_description_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateDescriptionErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_display_name_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_is_system_default_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateIsSystemDefaultErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_kind_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_labels_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_lead_time_days_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_name_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_non_field_errors_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_note_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_notice_required_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_platform_service_error_component import (
            ApiV1MaintenanceWindowsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_provider_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_provider_id_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_provider_reference_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_reconciliation_enabled_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_sla_availability_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_sla_target_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_slo_availability_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_slo_target_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_target_availability_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_time_slots_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateTimeSlotsErrorComponent,
        )
        from ..models.api_v1_maintenance_windows_partial_update_tolerations_error_component import (
            ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateArchivedAtErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateArchivedReasonErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateDebugModeErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateDescriptionErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateDisplayNameErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateIsSystemDefaultErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateKindErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateLabelsErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateNameErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdatePlatformServiceErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateProviderErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateProviderIdErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateProviderReferenceErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateSlaTargetErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateSloTargetErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateTimeSlotsErrorComponent
                | ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_0 = (
                        ApiV1MaintenanceWindowsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_1 = (
                        ApiV1MaintenanceWindowsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_2 = (
                        ApiV1MaintenanceWindowsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_3 = (
                        ApiV1MaintenanceWindowsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_4 = (
                        ApiV1MaintenanceWindowsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_5 = (
                        ApiV1MaintenanceWindowsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_6 = (
                        ApiV1MaintenanceWindowsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_7 = (
                        ApiV1MaintenanceWindowsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_8 = (
                        ApiV1MaintenanceWindowsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_9 = (
                        ApiV1MaintenanceWindowsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_10 = (
                        ApiV1MaintenanceWindowsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_11 = (
                        ApiV1MaintenanceWindowsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_12 = (
                        ApiV1MaintenanceWindowsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_13 = (
                        ApiV1MaintenanceWindowsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_14 = (
                        ApiV1MaintenanceWindowsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_15 = (
                        ApiV1MaintenanceWindowsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_16 = (
                        ApiV1MaintenanceWindowsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_17 = (
                        ApiV1MaintenanceWindowsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_18 = (
                        ApiV1MaintenanceWindowsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_19 = (
                        ApiV1MaintenanceWindowsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_20 = (
                        ApiV1MaintenanceWindowsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_21 = (
                        ApiV1MaintenanceWindowsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_22 = (
                        ApiV1MaintenanceWindowsPartialUpdateIsSystemDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_23 = (
                        ApiV1MaintenanceWindowsPartialUpdateLeadTimeDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_24 = (
                        ApiV1MaintenanceWindowsPartialUpdateNoticeRequiredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_25 = (
                        ApiV1MaintenanceWindowsPartialUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_partial_update_error_type_26 = (
                        ApiV1MaintenanceWindowsPartialUpdateNoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenance_windows_partial_update_error_type_27 = (
                    ApiV1MaintenanceWindowsPartialUpdateTimeSlotsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenance_windows_partial_update_error_type_27

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenance_windows_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenance_windows_partial_update_validation_error.additional_properties = d
        return api_v1_maintenance_windows_partial_update_validation_error

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
