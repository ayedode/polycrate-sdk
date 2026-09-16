from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenance_windows_update_annotations_error_component import (
        ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_archived_at_error_component import (
        ApiV1MaintenanceWindowsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_archived_error_component import (
        ApiV1MaintenanceWindowsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_archived_reason_error_component import (
        ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_criticality_error_component import (
        ApiV1MaintenanceWindowsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_debug_mode_error_component import (
        ApiV1MaintenanceWindowsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_description_error_component import (
        ApiV1MaintenanceWindowsUpdateDescriptionErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_display_name_error_component import (
        ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_is_system_default_error_component import (
        ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_kind_error_component import (
        ApiV1MaintenanceWindowsUpdateKindErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_labels_error_component import (
        ApiV1MaintenanceWindowsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_lead_time_days_error_component import (
        ApiV1MaintenanceWindowsUpdateLeadTimeDaysErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_name_error_component import (
        ApiV1MaintenanceWindowsUpdateNameErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_non_field_errors_error_component import (
        ApiV1MaintenanceWindowsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_note_error_component import (
        ApiV1MaintenanceWindowsUpdateNoteErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_notice_required_error_component import (
        ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_platform_service_error_component import (
        ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_provider_error_component import (
        ApiV1MaintenanceWindowsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_provider_id_error_component import (
        ApiV1MaintenanceWindowsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_provider_reference_error_component import (
        ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_reconciliation_enabled_error_component import (
        ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_sla_availability_error_component import (
        ApiV1MaintenanceWindowsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_sla_target_error_component import (
        ApiV1MaintenanceWindowsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_slo_availability_error_component import (
        ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_slo_target_error_component import (
        ApiV1MaintenanceWindowsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_target_availability_error_component import (
        ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_time_slots_error_component import (
        ApiV1MaintenanceWindowsUpdateTimeSlotsErrorComponent,
    )
    from ..models.api_v1_maintenance_windows_update_tolerations_error_component import (
        ApiV1MaintenanceWindowsUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenanceWindowsUpdateValidationError")


@_attrs_define
class ApiV1MaintenanceWindowsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponent |
            ApiV1MaintenanceWindowsUpdateArchivedAtErrorComponent | ApiV1MaintenanceWindowsUpdateArchivedErrorComponent |
            ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponent |
            ApiV1MaintenanceWindowsUpdateCriticalityErrorComponent | ApiV1MaintenanceWindowsUpdateDebugModeErrorComponent |
            ApiV1MaintenanceWindowsUpdateDescriptionErrorComponent | ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponent
            | ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponent | ApiV1MaintenanceWindowsUpdateKindErrorComponent |
            ApiV1MaintenanceWindowsUpdateLabelsErrorComponent | ApiV1MaintenanceWindowsUpdateLeadTimeDaysErrorComponent |
            ApiV1MaintenanceWindowsUpdateNameErrorComponent | ApiV1MaintenanceWindowsUpdateNonFieldErrorsErrorComponent |
            ApiV1MaintenanceWindowsUpdateNoteErrorComponent | ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponent |
            ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponent | ApiV1MaintenanceWindowsUpdateProviderErrorComponent
            | ApiV1MaintenanceWindowsUpdateProviderIdErrorComponent |
            ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponent |
            ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponent |
            ApiV1MaintenanceWindowsUpdateSlaAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsUpdateSlaTargetErrorComponent |
            ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsUpdateSloTargetErrorComponent |
            ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponent |
            ApiV1MaintenanceWindowsUpdateTimeSlotsErrorComponent | ApiV1MaintenanceWindowsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponent
        | ApiV1MaintenanceWindowsUpdateArchivedAtErrorComponent
        | ApiV1MaintenanceWindowsUpdateArchivedErrorComponent
        | ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponent
        | ApiV1MaintenanceWindowsUpdateCriticalityErrorComponent
        | ApiV1MaintenanceWindowsUpdateDebugModeErrorComponent
        | ApiV1MaintenanceWindowsUpdateDescriptionErrorComponent
        | ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponent
        | ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponent
        | ApiV1MaintenanceWindowsUpdateKindErrorComponent
        | ApiV1MaintenanceWindowsUpdateLabelsErrorComponent
        | ApiV1MaintenanceWindowsUpdateLeadTimeDaysErrorComponent
        | ApiV1MaintenanceWindowsUpdateNameErrorComponent
        | ApiV1MaintenanceWindowsUpdateNonFieldErrorsErrorComponent
        | ApiV1MaintenanceWindowsUpdateNoteErrorComponent
        | ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponent
        | ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponent
        | ApiV1MaintenanceWindowsUpdateProviderErrorComponent
        | ApiV1MaintenanceWindowsUpdateProviderIdErrorComponent
        | ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponent
        | ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponent
        | ApiV1MaintenanceWindowsUpdateSlaAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsUpdateSlaTargetErrorComponent
        | ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsUpdateSloTargetErrorComponent
        | ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponent
        | ApiV1MaintenanceWindowsUpdateTimeSlotsErrorComponent
        | ApiV1MaintenanceWindowsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenance_windows_update_annotations_error_component import (
            ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_archived_at_error_component import (
            ApiV1MaintenanceWindowsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_archived_error_component import (
            ApiV1MaintenanceWindowsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_archived_reason_error_component import (
            ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_criticality_error_component import (
            ApiV1MaintenanceWindowsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_debug_mode_error_component import (
            ApiV1MaintenanceWindowsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_description_error_component import (
            ApiV1MaintenanceWindowsUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_display_name_error_component import (
            ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_is_system_default_error_component import (
            ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_kind_error_component import (
            ApiV1MaintenanceWindowsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_labels_error_component import (
            ApiV1MaintenanceWindowsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_lead_time_days_error_component import (
            ApiV1MaintenanceWindowsUpdateLeadTimeDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_name_error_component import (
            ApiV1MaintenanceWindowsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_non_field_errors_error_component import (
            ApiV1MaintenanceWindowsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_note_error_component import (
            ApiV1MaintenanceWindowsUpdateNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_notice_required_error_component import (
            ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_platform_service_error_component import (
            ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_provider_error_component import (
            ApiV1MaintenanceWindowsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_provider_id_error_component import (
            ApiV1MaintenanceWindowsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_provider_reference_error_component import (
            ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_reconciliation_enabled_error_component import (
            ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_sla_availability_error_component import (
            ApiV1MaintenanceWindowsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_sla_target_error_component import (
            ApiV1MaintenanceWindowsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_slo_availability_error_component import (
            ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_slo_target_error_component import (
            ApiV1MaintenanceWindowsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_target_availability_error_component import (
            ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_tolerations_error_component import (
            ApiV1MaintenanceWindowsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateLeadTimeDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateDescriptionErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenanceWindowsUpdateNoteErrorComponent):
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
        from ..models.api_v1_maintenance_windows_update_annotations_error_component import (
            ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_archived_at_error_component import (
            ApiV1MaintenanceWindowsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_archived_error_component import (
            ApiV1MaintenanceWindowsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_archived_reason_error_component import (
            ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_criticality_error_component import (
            ApiV1MaintenanceWindowsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_debug_mode_error_component import (
            ApiV1MaintenanceWindowsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_description_error_component import (
            ApiV1MaintenanceWindowsUpdateDescriptionErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_display_name_error_component import (
            ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_is_system_default_error_component import (
            ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_kind_error_component import (
            ApiV1MaintenanceWindowsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_labels_error_component import (
            ApiV1MaintenanceWindowsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_lead_time_days_error_component import (
            ApiV1MaintenanceWindowsUpdateLeadTimeDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_name_error_component import (
            ApiV1MaintenanceWindowsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_non_field_errors_error_component import (
            ApiV1MaintenanceWindowsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_note_error_component import (
            ApiV1MaintenanceWindowsUpdateNoteErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_notice_required_error_component import (
            ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_platform_service_error_component import (
            ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_provider_error_component import (
            ApiV1MaintenanceWindowsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_provider_id_error_component import (
            ApiV1MaintenanceWindowsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_provider_reference_error_component import (
            ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_reconciliation_enabled_error_component import (
            ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_sla_availability_error_component import (
            ApiV1MaintenanceWindowsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_sla_target_error_component import (
            ApiV1MaintenanceWindowsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_slo_availability_error_component import (
            ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_slo_target_error_component import (
            ApiV1MaintenanceWindowsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_target_availability_error_component import (
            ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_time_slots_error_component import (
            ApiV1MaintenanceWindowsUpdateTimeSlotsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_maintenance_windows_update_tolerations_error_component import (
            ApiV1MaintenanceWindowsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponent
                | ApiV1MaintenanceWindowsUpdateArchivedAtErrorComponent
                | ApiV1MaintenanceWindowsUpdateArchivedErrorComponent
                | ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponent
                | ApiV1MaintenanceWindowsUpdateCriticalityErrorComponent
                | ApiV1MaintenanceWindowsUpdateDebugModeErrorComponent
                | ApiV1MaintenanceWindowsUpdateDescriptionErrorComponent
                | ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponent
                | ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponent
                | ApiV1MaintenanceWindowsUpdateKindErrorComponent
                | ApiV1MaintenanceWindowsUpdateLabelsErrorComponent
                | ApiV1MaintenanceWindowsUpdateLeadTimeDaysErrorComponent
                | ApiV1MaintenanceWindowsUpdateNameErrorComponent
                | ApiV1MaintenanceWindowsUpdateNonFieldErrorsErrorComponent
                | ApiV1MaintenanceWindowsUpdateNoteErrorComponent
                | ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponent
                | ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponent
                | ApiV1MaintenanceWindowsUpdateProviderErrorComponent
                | ApiV1MaintenanceWindowsUpdateProviderIdErrorComponent
                | ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponent
                | ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponent
                | ApiV1MaintenanceWindowsUpdateSlaAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsUpdateSlaTargetErrorComponent
                | ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsUpdateSloTargetErrorComponent
                | ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponent
                | ApiV1MaintenanceWindowsUpdateTimeSlotsErrorComponent
                | ApiV1MaintenanceWindowsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_0 = (
                        ApiV1MaintenanceWindowsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_1 = (
                        ApiV1MaintenanceWindowsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_2 = (
                        ApiV1MaintenanceWindowsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_3 = (
                        ApiV1MaintenanceWindowsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_4 = (
                        ApiV1MaintenanceWindowsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_5 = (
                        ApiV1MaintenanceWindowsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_6 = (
                        ApiV1MaintenanceWindowsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_7 = (
                        ApiV1MaintenanceWindowsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_8 = (
                        ApiV1MaintenanceWindowsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_9 = (
                        ApiV1MaintenanceWindowsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_10 = (
                        ApiV1MaintenanceWindowsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_11 = (
                        ApiV1MaintenanceWindowsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_12 = (
                        ApiV1MaintenanceWindowsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_13 = (
                        ApiV1MaintenanceWindowsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_14 = (
                        ApiV1MaintenanceWindowsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_15 = (
                        ApiV1MaintenanceWindowsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_16 = (
                        ApiV1MaintenanceWindowsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_17 = (
                        ApiV1MaintenanceWindowsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_18 = (
                        ApiV1MaintenanceWindowsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_19 = (
                        ApiV1MaintenanceWindowsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_20 = (
                        ApiV1MaintenanceWindowsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_21 = (
                        ApiV1MaintenanceWindowsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_22 = (
                        ApiV1MaintenanceWindowsUpdateIsSystemDefaultErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_23 = (
                        ApiV1MaintenanceWindowsUpdateLeadTimeDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_24 = (
                        ApiV1MaintenanceWindowsUpdateNoticeRequiredErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_25 = (
                        ApiV1MaintenanceWindowsUpdateDescriptionErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenance_windows_update_error_type_26 = (
                        ApiV1MaintenanceWindowsUpdateNoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenance_windows_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenance_windows_update_error_type_27 = (
                    ApiV1MaintenanceWindowsUpdateTimeSlotsErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenance_windows_update_error_type_27

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenance_windows_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenance_windows_update_validation_error.additional_properties = d
        return api_v1_maintenance_windows_update_validation_error

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
